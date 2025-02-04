from django.urls import path,include
from . import views  
from .views import signup
from django.contrib.auth.views import (LoginView, LogoutView ,PasswordChangeView, 
       PasswordChangeDoneView,  PasswordResetView,
       PasswordResetDoneView,
       PasswordResetConfirmView,
       PasswordResetCompleteView)


urlpatterns = [  
    path('', views.home, name='home'),

    path('about', views.about, name='about'),

    path('projects/', views.projects, name='projects'),

    path('portfolio', views.portfolio, name='portfolio'),

    path('weblog',views.weblog, name="weblog"),

    path('services', views.services,name="services"),
    
    path('contact', views.contact, name='contact'),

    path("signup/", signup, name="signup"),

    path('login/', LoginView.as_view(template_name='nasrat_website/login.html'), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('password_change/', PasswordChangeView.as_view(template_name='nasrat_website/password_change.html'), name='password_change'),

    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='nasrat_website/password_change_done.html'), name='password_change_done'),

    path('password_reset/', PasswordResetView.as_view(template_name='nasrat_website/password_reset.html'), name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='nasrat_website/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='nasrat_website/password_reset_confirm.html'), name='password_reset_confirm'),

    path('reset/done/', PasswordResetCompleteView.as_view(template_name='nasrat_website/password_reset_complete.html'), name='password_reset_complete'),



]