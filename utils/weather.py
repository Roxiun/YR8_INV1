import geocoder
from geopy.geocoders import Nominatim

def getWeather(location: str = None):
    if not location:
        g = geocoder.ip('me')
        cord = ', '.join([str(item) for item in g.latlng])
        geolocator = Nominatim(user_agent="yr8inv1")
        location = geolocator.reverse(cord)