import Adafruit_DHT
import time
import datetime
class WeatherStation:
    def __init__(self):
        self.DHT_SENSOR = Adafruit_DHT.DHT22
        self.DHT_PIN = 4
        
    def get_weather_data(self):
        humidity, temperature = Adafruit_DHT.read(self.DHT_SENSOR, self.DHT_PIN)
        date = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        if humidity is not None and temperature is not None:
            return WeatherData(temperature, humidity, date)
        else:
            return None

class WeatherData:
    def __init__(self, temperature, humidity, date):
        self.temperature = temperature
        self.humidity = humidity
        self.date = date
    
    def to_json(self):
        return '{{"temperature": {temperature}, "humidity": {humidity}, "timestamp":{date}}}'.format( \
            temperature = self.temperature, humidity = self.humidity, date = self.date)

