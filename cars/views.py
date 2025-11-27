from django.shortcuts import render
from .models import Car
from django.shortcuts import get_object_or_404
# Create your views here.
def cars(request):
    cars_list = Car.objects.all()
    context = {
        "cars": cars_list
    }
    return render(request, "cars/cars.html", context)

def car_detail(request, car_id):
    car = get_object_or_404(Car, car_id=car_id)
    context = {
        'car': car,
    }
    return render(request, 'cars/car_detail.html', context)
