from django import forms
from django.forms.widgets import SelectDateWidget
from .widgets import RangeInput
import datetime

class WeatherForm(forms.Form):
    """Collect information about types of weather anomalies wanted."""
    lat = forms.FloatField(
        initial=0,
        widget=forms.HiddenInput()
    )
    lon = forms.FloatField(
        initial=0,
        widget=forms.HiddenInput()
    )
    radius = forms.IntegerField(
        label='Radius(km)',
        initial=1000,
        widget=RangeInput(attrs={'min': 0, 'max': 10000})
    )
    start_date = forms.DateField(
        label='Start Date',
        initial=datetime.date(2010, 1, 1),
        widget=SelectDateWidget(years=range(2000, 2024))
    )
    end_date = forms.DateField(
        label='End Date',
        initial=datetime.date(2023, 2, 1),
        widget=SelectDateWidget(years=range(2000, 2024))
    )