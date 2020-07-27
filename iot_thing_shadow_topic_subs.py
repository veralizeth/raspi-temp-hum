from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import json
import datetime

topic = "$aws/things/Tempo/shadow/update"

def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

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
if myAWSIoTMQTTClient.connect():
  print('AWS connection succeeded')

# Publish to the same topic in a loop forever
loopCount = 0
while True:
    myAWSIoTMQTTClient.subscribe("$aws/things/Tempo/shadow/update", 1, customCallback)
    message = {}
    message['sequence'] = loopCount
    messageJson = json.dumps(message)
    loopCount += 1
    time.sleep(1)
