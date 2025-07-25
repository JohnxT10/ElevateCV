from django import forms
from .models import CV, Education, Experience, Skill, Project

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['title']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'degree', 'start_year', 'end_year']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company', 'position', 'start_year', 'end_year', 'description']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'level']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']