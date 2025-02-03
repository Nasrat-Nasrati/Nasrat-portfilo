from django.urls import path,include
from nasrat_website import views


urlpatterns = [
    path('', views.home, name='home'),
]
