# BDA-Assignment
# BDA Weather Data MapReduce

This repository contains a MapReduce program to analyze weather data. It processes hourly weather sensor logs to extract meaningful insights.

## Problem Statement

Write a MapReduce program that mines weather data. Weather sensors collecting data every hour at many locations across the globe gather a large volume of log data, which is a good candidate for analysis with MapReduce, since it is semi-structured and record-oriented.

## Data

The `data/weather_data.csv` file contains sample weather data. Each row represents a weather reading. The columns are:

-   `location`: Location of the sensor.
-   `timestamp`: Timestamp of the reading (YYYY-MM-DD HH:MM:SS).
-   `temperature`: Temperature in Celsius.
-   `humidity`: Humidity percentage.

## MapReduce Program

The program consists of two main parts:

-   `weather_mapper.py`: Maps each weather reading to a key-value pair.
-   `weather_reducer.py`: Reduces the mapped data to produce aggregated results.

## Usage

1.  Place your weather data in `data/weather_data.csv`.
2.  Run the MapReduce program using Hadoop Streaming or a similar framework.

    ```bash
    hadoop jar /path/to/hadoop-streaming.jar \
    -input data/weather_data.csv \
    -output output \
    -mapper src/weather_mapper.py \
    -reducer src/weather_reducer.py
    ```

## Example Data (data/weather_data.csv)

```csv
location,timestamp,temperature,humidity
New York,2023-10-26 00:00:00,15,60
London,2023-10-26 00:00:00,10,70
New York,2023-10-26 01:00:00,16,62
London,2023-10-26 01:00:00,11,72
New York,2023-10-26 02:00:00,14,65
London,2023-10-26 02:00:00,9,75
