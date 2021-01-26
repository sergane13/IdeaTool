from .models import *
from django.forms import ModelForm


class CreateIdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = '__all__'


class CreateOpinionForm(ModelForm):
    class Meta:
        model = Opinions
        fields = '__all__'
