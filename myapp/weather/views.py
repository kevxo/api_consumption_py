from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from weather.models import Forecast
from weather.helpers.weather_api import get_data
from weather.helpers.queries.find_by_location import location_exist

def create(request):
    location = request.GET.get('location')
    print(location, 'LOOKHERE')

    if not location:
        return HttpResponse("Bad Request. Make sure location parameter is included", status=400)

    location_found = location_exist(location.capitalize())

    if location_found:
        return HttpResponse("Data already exists!")

    data = get_data(location)

    location = data["location"]["name"]
    farenheit = data["current"]["temperature"]
    celcius = int((farenheit - 32) * 5/9)


    forecast = Forecast(location=location, temp_in_f=str(farenheit), temp_in_c=str(celcius))

    forecast.save()

    return HttpResponse(f"Forecast Record Created {forecast.uuid}")
