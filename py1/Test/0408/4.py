from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="seuni")
location = geolocator.geocode("Siheung South Korea")
print(location)

print(location.latitude, location.longitude)
print(location.raw)