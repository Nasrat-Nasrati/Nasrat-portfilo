from django.http import HttpResponse
from django.shortcuts import render

# Home View
def home(request):
    return render(request, 'nasrat_website/home.html')

# About Views
def about_list(request):
    return render(request, 'nasrat_website/about.html')

def about_detail(request, pk):
    return HttpResponse(f"This is the About Detail page for ID {pk}.")

def about_create(request):
    return HttpResponse("This is the About Create page.")

def about_update(request, pk):
    return HttpResponse(f"This is the About Update page for ID {pk}.")

def about_delete(request, pk):
    return HttpResponse(f"This is the About Delete page for ID {pk}.")

# Project Views
def project_list(request):
   return render(request, 'nasrat_website/projects.html')

def project_detail(request, pk):
    return HttpResponse(f"This is the Project Detail page for ID {pk}.")

def project_create(request):
    return HttpResponse("This is the Project Create page.")

def project_update(request, pk):
    return HttpResponse(f"This is the Project Update page for ID {pk}.")

def project_delete(request, pk):
    return HttpResponse(f"This is the Project Delete page for ID {pk}.")

# Additional Views (for resume, portfolio, etc.)
def resume(request):
    return render(request, 'nasrat_website/resume.html')

def portfolio(request):
    return render(request, 'nasrat_website/portfolio.html')

def skills(request):
    return render(request, 'nasrat_website/skills.html')

def services(request):
    return render(request, 'nasrat_website/services.html')

def achievement(request):
    return render(request, 'nasrat_website/achivement.html')

def stats(request):
    return render(request, 'nasrat_website/stats.html')

def weblog(request):
    return render(request, 'nasrat_website/weblog.html')

def contact(request):
    return render(request, 'nasrat_website/contact.html')
