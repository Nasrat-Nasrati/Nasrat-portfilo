from django.urls import path,include
from . import views  

urlpatterns = [  
    path('', views.home, name='home'),

    path('about', views.about, name='about'),

    path('projects/', views.projects, name='projects'),

    path('portfolio', views.portfolio, name='portfolio'),

    path('weblog',views.weblog, name="weblog"),

    path('services', views.services,name="services"),
    
    path('contact', views.contact, name='contact'),

]