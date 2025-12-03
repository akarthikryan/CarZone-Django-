from django.shortcuts import render
from cars.models import Car
from teams.models import TeamMember
from django.db.models import Q

def home(request):
    cars = []  # your existing cars context
    team_members = TeamMember.objects.all()  # fetch all team members
    return render(request, 'pages/home.html', {"cars": cars, "team_members": team_members})


def contact(request):
    return render(request, 'pages/contact.html')


def search(request):
    cars = Car.objects.all()

    keyword = request.GET.get('keyword')
    if keyword:
        cars = cars.filter(
            Q(car_name__icontains=keyword) |
            Q(description__icontains=keyword)
        )

    return render(request, 'cars/search.html', {"cars": cars})

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

# pages/views.py
def signup(request):
    return render(request, 'pages/signup.html')

def login(request):
    return render(request, 'pages/login.html')
