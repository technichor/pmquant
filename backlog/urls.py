from django.urls import path, include
from backlog.views import ideas_home, idea_list, idea_detail, idea_rank_pairwise, IdeaCreate

app_name = 'backlog'

urlpatterns = [
    path('ideas/list/', idea_list, name='idea_list'),
    path('idea/<page_slug>/', idea_detail, name='idea_detail'),
    path('ideas/add/', IdeaCreate.as_view(), name='idea-add'),
    path('ideas/rank/pairwise/', idea_rank_pairwise, name='idea-pairwise'),
    path('ideas/add/add_success/<page_slug>/', idea_detail, name='add_success'),
    path('ideas/', ideas_home, name='ideas_home'),
    #path('', include('home.urls'))
]
