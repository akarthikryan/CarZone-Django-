from django.shortcuts import render, get_object_or_404
from .models import Car
from django.db.models import Q

def cars(request):
    cars_list = Car.objects.all().order_by('-created_date')
    context = {
        "cars": cars_list,
    }
    return render(request, "cars/cars.html", context)


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    context = {
        "car": car
    }
    return render(request, "cars/car_detail.html", context)


def search(request):
    cars = Car.objects.all()

    keyword = request.GET.get("keyword")
    if keyword:
        cars = cars.filter(
            Q(car_name__icontains=keyword) |
            Q(description__icontains=keyword)
        )

    context = {
        "cars": cars,
        "keyword": keyword
    }
    return render(request, "cars/search.html", context)
