from django.shortcuts import render
from .forms import CalculatorForm

# Create your views here.


def calculator_forms(request):
    form = CalculatorForm
    context = {
     'form': form
    }
    return render(request, "fuelcalc/calculator.html", context)


# def calculating(request):
