from django.forms import ModelForm
from .models import Project

class ProjectFom(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude =['vote_total','vote_ratio','demo_link','source_link']