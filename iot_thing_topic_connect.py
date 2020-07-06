
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import weather_station_reporter
import logging
from time import sleep
import json
import datetime

clientId = "mypythoncodetempo"
thingName = "Tempo"
myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(
    "a2dixiflmrhbet-ats.iot.us-east-2.amazonaws.com", 8883)
myAWSIoTMQTTClient.configureCredentials(
    "./certs/AmazonRootCA1.pem", "./certs/5e3cf63a5a-private.pem.key", "./certs/5e3cf63a5a-certificate.pem.crt")

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect to AWS IoT
myAWSIoTMQTTClient.connect()
myAWSIoTMQTTClient.publish("raspi/temphum", "connected", 0)

while True:
    now = now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    ws = weather_station_reporter.WeatherStation()
    w_data = ws.get_weather_data()

    # Create message payload
    if w_data is not None:
        # payload = {"state": {"reported": {
        #     "temperature": w_data.temperature, "humidity": w_data.humidity, "isOn": True}}}
        print(w_data.to_json())
        myAWSIoTMQTTClient.publish("raspi/temphum", w_data.to_json(), 0)
        sleep(4)
    else:
      print("unable to connect")
