from django import forms
from .models import Car


class CalculatorForm(forms.Form):
        start_city = forms.CharField(label="City A", max_length=40, required=False)
        destination_city = forms.CharField(label="City B", max_length=40, required=False)
        distance = forms.DecimalField(label="Distance to travel", max_digits=10, decimal_places=2, required=True)
        petrol_price = forms.DecimalField(label="Petrol price", max_digits=10, decimal_places=2, required=True)
        car_consumption = forms.DecimalField(label="Car consumption l/100km", max_digits=10, decimal_places=2, required=True)


