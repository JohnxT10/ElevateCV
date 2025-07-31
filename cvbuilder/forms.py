from django import forms
from .models import CV, Education, WorkHistory, Qualification, Skill, Project

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['title', 'first_name', 'Surname' 'email', 'phone', 'address', 'summary']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'degree', 'start_year', 'end_year']

class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = ['name', 'institution', 'year']

class WorkHistoryForm(forms.ModelForm):
    class Meta:
        model = WorkHistory
        fields = ['company', 'position', 'start_year', 'end_year', 'description']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'level']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']