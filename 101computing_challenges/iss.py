import requests

parameters = {"lat": 37.78, "lon": -122.41}

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

data = response.json()
print(type(data))
print(data)