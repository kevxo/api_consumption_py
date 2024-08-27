from weather.models import Forecast

def location_exist(location: str) -> bool:
    data = Forecast.objects.filter(location=location).values().first()

    if data and data.get("uuid"):
        return True

    return False