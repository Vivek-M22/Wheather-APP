import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textField.get()
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=YOUR API"

    try:
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        # Sunrise and sunset times are in UTC, converting to local time can be complex
        # This is a simplified representation
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

        final_info = condition + "\n" + str(temp) + "°C"
        final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
        label1.config(text=final_info)
        label2.config(text=final_data)
    except KeyError:
        label1.config(text="Error")
        label2.config(text="City Not Found. Please check the spelling.")
    except requests.exceptions.ConnectionError:
        label1.config(text="Error")
        label2.config(text="Cannot connect to the internet.")


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
