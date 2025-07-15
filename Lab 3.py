#Chris Smith
#07/14/2025
#Chapter 12 Lab 3

import requests

zip_code = input("Enter ZIP code: ")

api_key = "6ca6c0375cc8a0ea0b4580e566efdbb7"

url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&units=imperial&appid={api_key}"

response = requests.get(url)

if response:
    response_dict = response.json()

    city = response_dict["name"]
    weather = response_dict["weather"][0]["description"].title()
    temp = round(response_dict["main"]["temp"])
    feels_like = round(response_dict["main"]["feels_like"])
    humidity = response_dict["main"]["humidity"]
    wind_speed = round(response_dict["wind"]["speed"])
    wind_deg = response_dict["wind"]["deg"]

    print()
    print(f"Current Weather for {city}:")
    print(f"Conditions: {weather}")
    print(f"Temperature: {temp} Degrees")
    print(f"Feels Like: {feels_like} Degrees")
    print(f"Humidity: {humidity}%")
    print(f"Wind: {wind_speed} knots @ {wind_deg} degrees")

else:
    print("Error: Unable to retrieve weather data.")

