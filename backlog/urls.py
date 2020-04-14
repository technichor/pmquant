from django.urls import path, include
from backlog.views import idea_sample_rank, idea_home, idea_list, idea_detail, idea_pairwise, choose_pairwise, IdeaCreate

app_name = 'backlog'

urlpatterns = [
    path('idea/<page_slug>/', idea_detail, name='idea_detail'),
    path('ideas/list/', idea_list, name='idea_list'),
    path('ideas/add/', IdeaCreate.as_view(), name='idea_add'),
    path('ideas/add/add_success/<page_slug>/', idea_detail, name='add_success'),
    path('ideas/rank/pairwise/', idea_pairwise, name='idea_pairwise'),
    path('ideas/rank/sample/', idea_sample_rank, name='idea_sample_rank'),
    path('ideas/rank/pairwise/choose/<int:win_id>/<int:lose_id>/', choose_pairwise, name='choose_pairwise'),
    path('ideas/', idea_home, name='ideas_home'),
    #path('', include('home.urls'))
]
