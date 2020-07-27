

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import weather_station_reporter
import logging
import time
import json

# Shadow JSON schema:
#
# {
#   "state": {
#       "desired":{
#           "temperature":<INT VALUE>,
#           "humidity":<INT VALUE>
#           "isON":<BOOLEAN VALUE>
#           "timestamp": <DATE VALUE>
#       }
#   }
# }

# Function called when a shadow is updated


def customShadowCallback_Delta(payload, responseStatus, token):

    # Display status and data from update request
    if responseStatus == "timeout":
        print("Update request " + token + " time out!")

    if responseStatus == "accepted":
        payloadDict = json.loads(payload)
        deltaMessage = json.dumps(payloadDict["state"])
        print(deltaMessage)

        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print("Update request with token: " + token + " accepted!")
        print("temperature: " +
              str(payloadDict["state"]["reported"]["temperature"]))
        print("humidity: " + str(payloadDict["state"]["reported"]["humidity"]))
        print("timestamp: " +
              str(payloadDict["state"]["reported"]["timestamp"]))
        print("isOn: " + str(payloadDict["state"]["reported"]["isOn"]))
        print("~~~~~~~~~~~~~~~~~~~~~~~\n\n")

    if responseStatus == "rejected":
        print("Update request " + token + " rejected!")

# Function called when a shadow is deleted


def customShadowCallback_Delete(payload, responseStatus, token):

    # Display status and data from delete request
    if responseStatus == "timeout":
        print("Delete request " + token + " time out!")

    if responseStatus == "accepted":
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print("Delete request with token: " + token + " accepted!")
        print("~~~~~~~~~~~~~~~~~~~~~~~\n\n")

    if responseStatus == "rejected":
        print("Delete request " + token + " rejected!")


clientId = "mypythoncodetempo"
thingName = "Tempo"
myAWSIoTMQTTShadowClient = AWSIoTMQTTShadowClient(clientId)
myAWSIoTMQTTShadowClient.configureEndpoint(
    "a2dixiflmrhbet-ats.iot.us-east-2.amazonaws.com", 8883)
myAWSIoTMQTTShadowClient.configureCredentials(
    "./certs/AmazonRootCA1.pem", "./certs/5e3cf63a5a-private.pem.key", "./certs/5e3cf63a5a-certificate.pem.crt")

# AWSIoTMQTTShadowClient connection configuration
myAWSIoTMQTTShadowClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTShadowClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTShadowClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect to AWS IoT
myAWSIoTMQTTShadowClient.connect()

# Create a device shadow handler, use this to update and delete shadow document
deviceShadowHandler = myAWSIoTMQTTShadowClient.createShadowHandlerWithName(
    thingName, True)

# Delete current shadow JSON doc
deviceShadowHandler.shadowDelete(customShadowCallback_Delete, 5)

# Listen on deltas
print(deviceShadowHandler.shadowRegisterDeltaCallback)
print(customShadowCallback_Delta)
deviceShadowHandler.shadowRegisterDeltaCallback(customShadowCallback_Delta)

# Read data from moisture sensor and update shadow
while True:

    # ws = weather_station_reporter.WeatherStation()
    # w_data = ws.get_weather_data()

    # # Create message payload
    # if w_data is not None:
    #     payload = {"state": {"reported": {
    #         "temperature": w_data.temperature, "humidity": w_data.humidity, "timestamp": w_data.date, "isOn": True}}}

    # # Update shadow
    # deviceShadowHandler.shadowUpdate(json.dumps(
    #     payload), customShadowCallback_Update, 5)
    time.sleep(1)
