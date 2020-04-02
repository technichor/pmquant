from django.forms import ModelForm
from .models import ideas, pairwise_results

# class newIdeaForm(forms.ModelForm):
#     class Meta:
#         model = ideas
#         fields = ('title','description','author','status')

# class ChooseForm(ModelForm):
#     #def __init__(self, )
#     class Meta:
#         model = pairwise_results
#         fields = ('win_idea', 'lose_idea')