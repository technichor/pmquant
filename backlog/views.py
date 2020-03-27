from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import ideas
# from .forms import newIdeaForm

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