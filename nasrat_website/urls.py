from django.urls import path,include
from . import views  


urlpatterns = [  
    path('', views.home, name='home'),

    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('projects/', views.projects, name='projects'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('weblog/', views.weblog, name='weblog'),
    path('achievement/', views.achievement, name='achievement'),
    path('skills/', views.skills, name='skills'),
    path('stats/', views.stats, name='stats'),


]