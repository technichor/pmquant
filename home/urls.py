from django.urls import path, include
from . import views
from home.views import AboutView, HomeView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    #path('backlog/', include('backlog.urls'))
    path('about/', AboutView.as_view(), name='about'),
]
