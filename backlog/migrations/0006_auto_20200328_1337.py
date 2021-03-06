# Generated by Django 3.0.4 on 2020-03-28 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backlog', '0005_pairwise_results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pairwise_results',
            name='lose_idea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lose_idea_name', to='backlog.ideas'),
        ),
        migrations.AlterField(
            model_name='pairwise_results',
            name='win_idea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='win_idea_name', to='backlog.ideas'),
        ),
    ]
