
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

def index(request):
    return render(request, 'home/base.html')

class AboutView(TemplateView):
    template_name="home/about.html"

class HomeView(TemplateView):
    template_name="home/home.html"