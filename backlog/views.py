from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import ideas

def idea_list(request):
    open_ideas = ideas.published.all()
#    template = loader.get_template()
    context = {'open_ideas': open_ideas}
    return render(request, 'backlog/idea_list.html', context)
#   return HttpResponse(template.render(context, request))

def idea_detail(request, page_slug):
    idea_details = get_object_or_404(ideas, slug=page_slug)
    context = {'idea_details': idea_details}
    return render(request, 'backlog/idea_detail.html', context)
