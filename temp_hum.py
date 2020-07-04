import Adafruit_DHT
import time

class WeatherStation:
    def __init__(self):
        self.DHT_SENSOR = Adafruit_DHT.DHT22
        self.DHT_PIN = 4
        
    def get_weather_data(self):
        humidity, temperature = Adafruit_DHT.read(self.DHT_SENSOR, self.DHT_PIN)
        if humidity is not None and temperature is not None:
            return WeatherData(temperature, humidity)
        else:
            return None

class WeatherData:
    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
    
    def to_json(self):
        return '{{"temperature": {temperature}, "humidity": {humidity}}}'.format( \
            temperature = self.temperature, humidity = self.humidity)
        

