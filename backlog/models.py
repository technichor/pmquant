from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.urls import reverse, reverse_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status=1)

# Create your models here.
class ideas(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    author = models.EmailField()
    elo_score = models.SmallIntegerField(default=1500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    release = models.CharField(max_length=10, blank=True)
    s_in_review = 0
    s_open = 1
    s_rejected = 2
    s_completed = 3
    s_choices = (
        (s_in_review, _('In Review')),
        (s_open, _('Open')),
        (s_rejected, _('Rejected')),
        (s_completed, _('Completed')),
    )
    status = models.PositiveSmallIntegerField(
        choices=s_choices,
        default=s_in_review,
    )
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name_plural = "ideas"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ideas, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('backlog:idea-detail', args=[self.slug])


class pairwise_results(models.Model):
    win_idea = models.ForeignKey(ideas, on_delete=models.CASCADE, related_name='win_idea_name')
    lose_idea = models.ForeignKey(ideas, on_delete=models.CASCADE, related_name='lose_idea_name')
    datetime = models.DateTimeField(auto_now_add=True)
    win_elo = models.SmallIntegerField(default=1500)
    lose_elo = models.SmallIntegerField(default=1500)
    new_win_elo = models.SmallIntegerField(default=1500)
    new_lose_elo = models.SmallIntegerField(default=1500)
    def win_elo_transformed(self):
        return 10**(self.win_elo/400) #hard-coded variable
    def lose_elo_transformed(self):
        return 10**(self.lose_elo/400) #hard-coded variable
    def win_expected(self):
        return self.win_elo_transformed()/(self.win_elo_transformed()+self.lose_elo_transformed())
    def lose_expected(self):
        return self.lose_elo_transformed()/(self.win_elo_transformed()+self.lose_elo_transformed())
    def win_elo_new(self):
        return self.win_elo+25*(1-self.win_expected())
    def lose_elo_new(self):
        return self.lose_elo+25*(0-self.win_expected())

    def __str__(self):
        return self.datetime.strftime("%m/%d/%Y, %H:%M:%S")
    
    def save(self, *args, **kwargs):
        self.new_win_elo = self.win_elo_new()
        self.new_lose_elo = self.lose_elo_new()
        super(pairwise_results, self).save(*args, **kwargs)


@receiver(post_save, sender=pairwise_results)
def update_elo(sender, instance, **kwargs):
    if kwargs.get('created', False):
        # win_up = ideas.objects.get(id=instance.win_idea.id)
        # lose_up = ideas.objects.get(id=instance.lose_idea.id)
        ideas.objects.filter(pk=instance.win_idea.id).update(elo_score=instance.new_win_elo)
        ideas.objects.filter(pk=instance.lose_idea.id).update(elo_score=instance.new_lose_elo)
        # ideas.objects.filter(pk=win_up.id).update(elo_score=kwargs.get('instance'))

#post_save.connect(update_elo, sender=pairwise_results)