from django.shortcuts import render  
from django.http import HttpResponse  
from .models import About,Projects,Portfolio,Services

def home(request):
    return render(request, 'nasrat_website/home.html')

def about(request):
    about = About.objects.first()
    return render(request,'nasrat_website/about.html',{'about': about})
    

def projects(request):
   projects = Projects.objects.all()
   return render(request, 'nasrat_website/projects.html', {'projects': projects})



def portfolio(request):
    portfolio = Portfolio.objects.first()  # Fetch the first portfolio (or filter as needed)
    return render(request, 'nasrat_website/protfilo.html', {'portfolio': portfolio})



def weblog(request):
    return render(request,'nasrat_website/weblog.html')





def services(request):
    services = Services.objects.all().order_by('order')
    return render(request, 'nasrat_website/services.html', {'services': services})



def contact(request):
    return HttpResponse("the contact will comming as soon as possbile")

