from django.shortcuts import render
from .forms import CalculatorForm

# Create your views here.


def calculator_forms(request):
    journey_cost = 0
    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            distance = form.cleaned_data['distance']
            petrol_price = form.cleaned_data['petrol_price']
            car_consumption = form.cleaned_data['car_consumption']
            journey_cost = (distance * car_consumption) / 100 * petrol_price
    else:
        form = CalculatorForm()

    context = {'form': form,
               'journey_cost': journey_cost}

    return render(request, "fuelcalc/calculator.html", context)




# def calculating(request):
