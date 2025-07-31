from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_list, name='cv_list'),
    # linked in the views.py file
    path('create/', views.cv_create, name='cv_create'),
    path('public/', views.public_cv_builder, name='public_cv_builder'),
    path('<int:pk>/edit/', views.cv_edit, name='cv_edit'),
    path('<int:pk>/delete/', views.cv_delete, name='cv_delete'),
]