# src/weather_mapper.py
import sys

for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith("location"):
        continue  # Skip header or empty lines
    location, timestamp, temperature, humidity = line.split(",")
    print(f"{location}\t{temperature}\t{humidity}")
