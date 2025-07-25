from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_list, name='cv_list'),
    path('create/', views.cv_create, name='cv_create'),
    path('<int:pk>/edit/', views.cv_edit, name='cv_edit'),
    path('<int:pk>/delete/', views.cv_delete, name='cv_delete'),
]