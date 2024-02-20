from geopy.geocoders import Nominatim

from rest_framework.exceptions import ValidationError


def get_location_info(latitude, longitude):
    geolocator = Nominatim(user_agent="your_geopy_app_name")
    location = geolocator.reverse((latitude, longitude), language="en")

    if location and "address" in location.raw:
        country = location.raw["address"].get("country", "")
        city = location.raw["address"].get("city", None)
        return country, city

    raise ValidationError({"error": "Can't find location"})
