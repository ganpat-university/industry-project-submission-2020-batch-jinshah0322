from datetime import datetime, timedelta
import random

class WeatherData:
    def __init__(self, temperature, humidity, wind_speed):
        self.timestamp = datetime.now()
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed

    def __str__(self):
        return f"Weather Data at {self.timestamp}: Temperature {self.temperature}°C, Humidity {self.humidity}%, Wind Speed {self.wind_speed} m/s"

class Sensor:
    def __init__(self, sensor_type):
        self.sensor_type = sensor_type

    def read_data(self):
        temperature = round(random.uniform(-10, 30), 2)
        humidity = round(random.uniform(0, 100), 2)
        wind_speed = round(random.uniform(0, 10), 2)
        return WeatherData(temperature, humidity, wind_speed)

class WeatherStation:
    def __init__(self, name):
        self.name = name
        self.sensors = []
        self.weather_data_history = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def collect_data(self):
        for sensor in self.sensors:
            weather_data = sensor.read_data()
            self.weather_data_history.append(weather_data)
            print(f"{self.name} collected data: {weather_data}")

    def analyze_trends(self):
        if not self.weather_data_history:
            print("No data available for analysis.")
            return

        latest_data = self.weather_data_history[-1]
        print(f"Latest Weather Data: {latest_data}")


    def provide_forecast(self):
        print(f"{self.name} Weather Forecast: Sunny with a chance of clouds.")

sensor1 = Sensor("Temperature and Humidity")
sensor2 = Sensor("Wind Speed")

weather_station = WeatherStation("City Weather Station")
weather_station.add_sensor(sensor1)
weather_station.add_sensor(sensor2)

weather_station.collect_data()
weather_station.analyze_trends()
weather_station.provide_forecast()
