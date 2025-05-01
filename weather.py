import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # For temperature in Celsius
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            'City': data['name'],
            'Temperature (°C)': data['main']['temp'],
            'Humidity (%)': data['main']['humidity'],
            'Weather': data['weather'][0]['description']
        }
        return weather
    else:
        return f"Error: {response.status_code}, {response.json().get('message', 'Failed to fetch data')}"

# Example usage
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    result = get_weather(city, api_key)
    print(result)
