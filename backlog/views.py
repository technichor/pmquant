from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import ideas, pairwise_results
import random
# from .forms import newIdeaForm

def idea_list(request):
    open_ideas = ideas.published.all()
    context = {'open_ideas': open_ideas}
    return render(request, 'backlog/idea_list.html', context)

def ideas_home(request):
    open_ideas = ideas.published.all()
    context = {'open_ideas': open_ideas}
    return render(request, 'backlog/ideas_home.html', context)

def idea_detail(request, page_slug):
    idea_details = get_object_or_404(ideas, slug=page_slug)
    context = {'idea_details': idea_details}
    return render(request, 'backlog/idea_detail.html', context)

def idea_rank_pairwise(request):
    last=ideas.published.count()-1
    index1 = random.randint(0,last)
    index2 = random.randint(0, last-1)
    if index2==index1: index2=last
    idea1 = ideas.published.all()[index1]
    idea2 = ideas.published.all()[index2]
    context = {'idea1': idea1, 'idea2': idea2}
    return render(request, 'backlog/ideas_rank_pairwise.html', context)

def choose_pairwise(request, win_id, lose_id):
    w_idea = get_object_or_404(ideas, id=win_id)
    l_idea = get_object_or_404(ideas, id=lose_id)
    new_choice = pairwise_results(win_idea=w_idea, lose_idea=l_idea, win_elo=w_idea.elo_score, lose_elo=l_idea.elo_score)
    new_choice.save()
    return redirect('backlog:idea_pairwise')

# def newIdea(request):
#     if request.method=='POST':
#         form = newIdeaForm(request.POST)
#         if form.is_valid():
#             new_idea = newIdeaForm.save()
#     else:
#         form = newIdeaForm()
#     return render(request, 'backlog/idea_create.html')

class IdeaCreate(CreateView):
    # template_name = 'backlog/ideas_form.html'
    model = ideas
    fields = ('title','description','author','status')
    success_url = reverse_lazy('backlog:idea_list')

