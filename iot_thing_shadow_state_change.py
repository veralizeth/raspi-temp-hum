from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import logging
import time
import json

clientId = "mypythoncodetempo"
thingName = "Tempo"
isOn=False
myAWSIoTMQTTShadowClient = AWSIoTMQTTShadowClient(clientId)
myAWSIoTMQTTShadowClient.configureEndpoint(
    "a2dixiflmrhbet-ats.iot.us-east-2.amazonaws.com", 8883)
myAWSIoTMQTTShadowClient.configureCredentials(
    "./certs/AmazonRootCA1.pem", "./certs/5e3cf63a5a-private.pem.key", "./certs/5e3cf63a5a-certificate.pem.crt")

# Connect to AWS IoT
myAWSIoTMQTTShadowClient.connect()

deviceShadowHandler = myAWSIoTMQTTShadowClient.createShadowHandlerWithName(
    thingName, True)

# Loop forever
while True:  # Run forever
  input_state = False
  if input_state == False:
    if isOn == False:
      print("turn on")
      newPayload = '{"state":{"desired":{"isOn":"true"}}}'
      deviceShadowHandler.shadowUpdate(newPayload, None, 5)
      isOn = True
    else:
      print("turn off")
      newPayload = '{"state":{"desired":{"isOn":"false"}}}'
      deviceShadowHandler.shadowUpdate(newPayload, None, 5)
      isOn = False
  time.sleep(0.2)  # Sleep for 0.2 second
