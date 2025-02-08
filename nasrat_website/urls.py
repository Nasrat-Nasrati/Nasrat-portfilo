from django.urls import path
from .views import (
    about_list, about_detail, about_create, about_update, about_delete,
    project_list, project_detail, project_create, project_update, project_delete,
    home, resume, portfolio, skills, services, achievement, stats, weblog, contact
)
from . import views

urlpatterns = [
    # Home URL
    path('', views.home, name="home"),

    # About URLs
    path('about/', about_list, name='about-list'),
    path('about/<int:pk>/', about_detail, name='about-detail'),
    path('about/create/', about_create, name='about-create'),
    path('about/<int:pk>/update/', about_update, name='about-update'),
    path('about/<int:pk>/delete/', about_delete, name='about-delete'),

    # Project URLs
    path('projects/', project_list, name='project-list'),
    path('projects/<int:pk>/', project_detail, name='project-detail'),
    path('projects/create/', project_create, name='project-create'),
    path('projects/<int:pk>/update/', project_update, name='project-update'),
    path('projects/<int:pk>/delete/', project_delete, name='project-delete'),

    # Additional URLs (from header)
    path('resume/', views.resume, name='resume'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('skills/', views.skills, name='skills'),
    path('services/', views.services, name='services'),
    path('achievement/', views.achievement, name='achievement'),
    path('stats/', views.stats, name='stats'),
    path('weblog/', views.weblog, name='weblog'),
    path('contact/', views.contact, name='contact'),
]
