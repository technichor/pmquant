from django.urls import path, include
from backlog.views import choose_pairwise, ideas_home, idea_list, idea_detail, idea_rank_pairwise, IdeaCreate

app_name = 'backlog'

urlpatterns = [
    path('idea/<page_slug>/', idea_detail, name='idea_detail'),
    path('ideas/list/', idea_list, name='idea_list'),
    path('ideas/add/', IdeaCreate.as_view(), name='idea_add'),
    path('ideas/add/add_success/<page_slug>/', idea_detail, name='add_success'),
    path('ideas/rank/pairwise/', idea_rank_pairwise, name='idea_pairwise'),
    path('ideas/rank/pairwise/choose/<int:win_id>/<int:lose_id>/', choose_pairwise, name='pairwise_choose'),
    path('ideas/', ideas_home, name='ideas_home'),
    #path('', include('home.urls'))
]
