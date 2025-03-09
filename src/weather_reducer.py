# src/weather_reducer.py

import sys

current_location = None
temperatures = []
humidities = []

for line in sys.stdin:
    line = line.strip()
    location, temperature, humidity = line.split("\t")
    try:
        temperature = float(temperature)
        humidity = float(humidity)
    except ValueError:
        continue

    if current_location == location:
        temperatures.append(temperature)
        humidities.append(humidity)
    else:
        if current_location:
            avg_temp = sum(temperatures) / len(temperatures)
            avg_humidity = sum(humidities) / len(humidities)
            print(f"{current_location},{avg_temp},{avg_humidity}")

        current_location = location
        temperatures = [temperature]
        humidities = [humidity]

if current_location:
    avg_temp = sum(temperatures) / len(temperatures)
    avg_humidity = sum(humidities) / len(humidities)
    print(f"{current_location},{avg_temp},{avg_humidity}")
