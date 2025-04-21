import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        print(f"Weather in {city_name}: {weather}")
        print(f"Temperature: {temp}°C, feels like {feels_like}°C")
    else:
        print("City not found or API request failed!")

# Replace with your actual API key
API_KEY = "your_openweathermap_api_key"
city = input("Enter city name: ")
get_weather(city, API_KEY)
