from django.db import models
from django.contrib.auth.models import User

# Main CV model, stores user and contact details
class CV(models.Model):
    TITLE_CHOICES = [
        ('Mr', 'Mr'),
        ('Ms', 'Ms'),
        ('Miss', 'Miss'),
        ('Mrs', 'Mrs'),
        ('Dr', 'Dr'),
        ('Prof', 'Prof'),
        ('Sir', 'Sir'),
        ('Mx', 'Mx'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)  # Dropdown for title
    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  

# Education section for a CV
class Education(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='education')  
    school = models.CharField(max_length=255)          
    degree = models.CharField(max_length=255)          
    start_year = models.IntegerField()                  
    end_year = models.IntegerField(blank=True, null=True)

# Qualifications section for a CV (certificates, licenses, etc.)
class Qualification(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='qualifications') 
    name = models.CharField(max_length=255)              
    institution = models.CharField(max_length=255, blank=True)  
    year = models.IntegerField(blank=True, null=True)    

# Work history section for a CV
class WorkHistory(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='work_history')  
    company = models.CharField(max_length=255)           
    position = models.CharField(max_length=255)          
    start_year = models.IntegerField()                  
    end_year = models.IntegerField(blank=True, null=True)  
    description = models.TextField(blank=True)           

# Skills section for a CV
class Skill(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='skills')  
    name = models.CharField(max_length=255)            
    level = models.CharField(max_length=50, blank=True) 

# Projects section for a CV
class Project(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='projects')  # Related CV
    title = models.CharField(max_length=255)             
    description = models.TextField(blank=True)          
    link = models.URLField(blank=True)                   

    def __str__(self):
        return self.title