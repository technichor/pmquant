from django.urls import path, include
from . import views

app_name = 'backlog'

urlpatterns = [
    path('list/', views.idea_list, name='idea_list'),
    path('idea/<page_slug>/', views.idea_detail, name='idea_detail'),
    #path('', include('home.urls'))
]
