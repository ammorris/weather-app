import tkinter as tk
import requests
import time

api_key = "0530f8c84301fe0e04d7290eccc73783"


def get_weather(canvas):
    city = city_textfield.get()
    state = state_textfield.get()
    country = country_textfield.get()

    first_api = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&appid={api_key}"
    first_json_data = requests.get(first_api).json()

    lat = first_json_data[0]["lat"]
    lon = first_json_data[0]["lon"]

    pacific_time_difference = 25200

    second_api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial"
    second_json_data = requests.get(second_api).json()

    condition = second_json_data["weather"][0]["main"]

    temp_fahrenheit = int(second_json_data["main"]["temp"])
    min_temp_fahrenheit = int(second_json_data["main"]["temp_min"])
    max_temp_fahrenheit = int(second_json_data["main"]["temp_max"])

    pressure = second_json_data["main"]["pressure"]
    humidity = second_json_data["main"]["humidity"]
    wind = second_json_data["wind"]["speed"]
    sunrise = time.strftime("%I:%M:%S %p", time.gmtime(second_json_data["sys"]["sunrise"] - pacific_time_difference))
    sunset = time.strftime("%I:%M:%S %p", time.gmtime(second_json_data["sys"]["sunset"] - pacific_time_difference))

    final_info = f"{condition}\n{str(temp_fahrenheit)}°F"
    final_data = f"""
    Max Temp: {str(max_temp_fahrenheit)}°F
    Min Temp: {str(min_temp_fahrenheit)}°F
    Pressure: {str(pressure)} hPa
    Humidity: {str(humidity)}%
    Wind Speed: {str(wind)} mph
    Sunrise: {str(sunrise)}
    Sunset: {str(sunset)}
    """
    label1.config(text=final_info)
    label2.config(text=final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

city_textfield = tk.Entry(canvas, font=t)
city_textfield.pack(pady=20)
city_textfield.focus()

state_textfield = tk.Entry(canvas, font=t)
state_textfield.pack(pady=20)

country_textfield = tk.Entry(canvas, font=t)
country_textfield.pack(pady=20)

country_textfield.bind("<Return>", get_weather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
