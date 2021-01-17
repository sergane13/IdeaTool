from .models import *
from django.forms import ModelForm


class CreateIdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = '__all__'
