from django.shortcuts import render, redirect

from .models import About,Projects,Portfolio,Services,Contact



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
    contact = Contact.objects.all().order_by('created_at')
    return render(request, 'nasrat_website/contact.html', {'contact': contact})


# View for Achievement Page
def achievement(request):
    return render(request, 'nasrat_website/achievement.html')

# View for Resume Page
def resume(request):
    return render(request, 'nasrat_website/resume.html')

# View for Skills Page
def skills(request):
    return render(request, 'nasrat_website/skills.html')

# View for Stats Page
def stats(request):
    return render(request, 'nasrat_website/stats.html')