from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from .models import About,Projects,Portfolio,Services,Contact
from django.contrib.auth.decorators import login_required


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



@login_required
def contact(request):
    contact = Contact.objects.all().order_by('created_at')
    return render(request, 'nasrat_website/contact_us.html', {'contact': contact})



def LogoutView(request):
    return render(request, 'nasrat_website/logout.html')
    


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signing up
            return redirect('home')  # Redirect to home or dashboard
    else:
        form = SignUpForm()
    
    return render(request, "nasrat_website/signup.html", {"form": form})
