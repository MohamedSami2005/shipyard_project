from django.shortcuts import render

def homepage(request):
    return render(request, 'home/home.html')  # Render the home page

def about(request):
    return render(request, 'home/about.html')  # Render the about page

def services_view(request):
    return render(request, 'services/services.html')