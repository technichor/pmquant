from django.urls import path, include
from backlog.views import idea_list, idea_detail, IdeaCreate

app_name = 'backlog'

urlpatterns = [
    path('list/', idea_list, name='idea_list'),
    path('idea/<page_slug>/', idea_detail, name='idea_detail'),
    path('ideas/add/', IdeaCreate.as_view(), name='idea-add'),
    path('ideas/add/add_success/<page_slug>/', idea_detail, name='add_success'),
    #path('', include('home.urls'))
]
