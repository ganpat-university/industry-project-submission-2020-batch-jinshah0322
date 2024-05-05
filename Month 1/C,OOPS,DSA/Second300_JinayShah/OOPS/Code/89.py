class WeatherData:
  def __init__(self, temperature, humidity, pressure):
      self.temperature = temperature
      self.humidity = humidity
      self.pressure = pressure

class WeatherStation:
  def __init__(self, id):
      self.id = id
      self.weather_data = []

  def update_weather(self, temperature, humidity, pressure):
      self.weather_data.append(WeatherData(temperature, humidity, pressure))

class Forecast:
  def __init__(self, weather_station):
      self.weather_station = weather_station

  def generate_forecast(self):
      latest_data = self.weather_station.weather_data[-1]
      return f"Temperature: {latest_data.temperature}, Humidity: {latest_data.humidity}, Pressure: {latest_data.pressure}"

station1 = WeatherStation(1)

station1.update_weather(27.8, 61, 1018)
station1.update_weather(26.9, 60, 1017)

forecast1 = Forecast(station1)

print(forecast1.generate_forecast())
