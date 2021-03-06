# Catapult Raspberry PI Environment Monitoring
### Capstone Project - Vera Rodriguez - Ada Developers' Academy

To execute this project there are three repositories: 

1. raspi-temp-hum -> Hardware and connections to AWS Iot and SQS. 
1. raspi-temp-hum-api -> [Java Spring boot API Server](https://github.com/veralizeth/raspi-temp-hum-api)
1. raspi-temp-hum-frontEnd -> [React front-End](https://github.com/veralizeth/raspi-temp-hum-frontEnd)

## 1. raspi-temp-hum -> Hardware and connections to AWS Iot and SQS. 

## Table of Contents

* [Introduction and Technologies](#Introduction-and-Technologies)
* [AWS IOT Internet of Things](#AWS-IOT-Internet-of-Things)
    * [DHT22 sensor Configurations](#DHT22-sensor-Configurations)
    * [AWS IoT Configurations](#AWS-IoT-Configurations)
    * [AWS Pyhton SDK IoT Configurations](#AWS-Pyhton-SDK-IoT-Configurations)
* [AWS Rules](#AWS-Rules)
* [AWS SQS](#AWS-SQS)

## Introduction and Technologies
**The problem**: 

Monitoring events
Controlling a GPIO pin
Monitoring temperature with the DHT22 sensor
Send information to the cloud

**The solution**: 
    
  * Monitoring events and controlling a GPI pin
    * Built with Python 3.7 
    * Data from the DTH22 sensor
    
  * AWS IOT (Internet of thins) Send data from the sensor to the cloud
    * Create a AWS Thing [Steps to create the certificates and the thing](https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-create-thing.html)
    * Built with Python 3.7 AWS SDK [Github repository](https://github.com/aws/aws-iot-device-sdk-python-v2)

## DHT22 Sensor

DHT22 — This temperature and humidity sensor has temperature accuracy of +/- 0.5 C and a humidity range from 0 to 100 percent. It is simple to wire up to the Raspberry Pi and doesn’t require any pull up resistors.

Example bellow:

![DHT22 sensor](/DTH22raspisensor.jpeg)

## AWS IOT Internet of Things

  * Key data: 
    * Certificates are used to authenticate the requests and it is must to activate the certificate before use it
    * Policies are used to check whether the requesting resources are authorized or not
    * Topics are not visible to the outside world. When you are publishing or subscribing to the topic you just have to mention a topic name accordingly. Now it all set in the AWS IoT end. In conclusion, we have created a thing. certificate and policy and then we have attached the thing and policy to the certificate.

### Use cases

AWS IoT makes it easy for you to build scalable IoT applications that collect, process, analyze, and act on data generated by connected home devices without having to manage any infrastructure. This helps you focus on building solutions and experiences that deliver value to both your businesses and your consumers and create a new class of connected home applications that interact with the physical world. [Iot Solutions](https://aws.amazon.com/iot/solutions/connected-home/?c=i&sec=uc2)

### Installation Instructions

#### DHT22 sensor Configurations: 

The DHT22 will have three pins — 5V, Gnd, and data. There should be a pin label for power on the DHT22 (e.g. ‘+’ or ‘5V’). Connect this to pin 2 (the top right pin, 5V) of the Pi. The Gnd pin will be labeled ‘-’ or ‘Gnd’ or something equivalent. Connect this to pin 6 Gnd (two pins below the 5V pin) on the Pi. The remaining pin on the DHT22 is the data pin and will be labeled ‘out’ or ‘s’ or ‘data’. Connect this to one of the GPIO pins on the Pi such as GPIO4 (pin 7). Once this is wired, power on your Pi.

Install the Adafruit DHT Python module at a command prompt to make reading DHT22 sensor data super easy:

```$ sudo pip install Adafruit_DHT```

With our operating system installed along with our two Python modules for reading sensor data and sending data to Initial State, we are ready to write our Python script. The following script will create/append to an Initial State data bucket, read the DHT22 sensor data, and send that data to a real-time dashboard. All you need to do is use the file in this repository called [weather_station_reporter.py](https://github.com/veralizeth/raspi-temp-hum/blob/master/weather_station_reporter.py)

#### AWS IoT Configurations
   * Thing
        Thing is representing the actual hardware device in the AWS IoT side. AWS IoT will provide the HTTPS endpoint to interact with the thing and to communicate with thing it is must to have a secure connection using SSL certificate.
        
   * Configuring a thing in the AWS IoT:
      1. Log in to the AWS console and then navigate to the IoT Core dashboard. Now click on the Manage -> Things link.
      1. Click on the create button to create a thing and follow the wizard. In the 2nd step click on the “Create thing without certificate” button.
      1. Now you should be able to view the created thing in the thing dashboard. 
      1. Click on the particular thing and inspect the options which are associated with the thing. To interact with the thing there is a HTTPS endpoint under the interact link.
      
   * Create AWS sign certificate:
      1. Click on the Secure -> Certificates link and then click in the create button on the IoT Core dashboard.
      1. As we are using the AWS sign certificate, now click on the “Create certificate” button. 
      1. Download the certificate, public key, private key and the root CA certificate by clicking each “Download” button in the new window. Also make sure to activate the certificate by clicking the “Activate” button.
      
   * Adding new policy:
     1. Click on the Secure -> Policies link and then click on the create button in the IoT Core dashboard.
     1. Name the policy and then add the below policy settings to it by using the advance mode option.
     
* Attaching Thing and Policy to the Certificate:
     1. Click on the Secure -> Certificates link to view the certificates list. Now by clicking the three dot mark on the relevant certificate you would be able to attach the thing and the policy to the given certificate.

#### AWS Pyhton SDK IoT Configurations 

Install Python 3.7

``` bash 
python ––version
sudo apt update
sudo apt install python 3.7
python ––version
```

Install from pip

``` bash
pip install AWSIoTPythonSDK
```

Use AWS SDK [Github repository](https://github.com/aws/aws-iot-device-sdk-python-v2)

To connect your rasperryPI with IOT use the file in this repo called: [iot_thing_shadow_reported.py](https://github.com/veralizeth/raspi-temp-hum/blob/master/iot_thing_shadow_reported.py) don’t forget to add your certificates.


## AWS Rules

### Use case

Rules give your devices the ability to interact with AWS services. Rules are analyzed and actions are performed based on the MQTT topic stream. You can use rules to support tasks like write data received from a device to an Amazon DynamoDB database,  Send a push notification to all users using Amazon SNS and many more. 

For the purpose of this project we are going to use AWS Rules to publish data to an Amazon SQS queue.

#### To create a new rule follow this tutorial: [Creating an AWS IoT rule](https://docs.aws.amazon.com/iot/latest/developerguide/iot-create-rule.html)

The rule should looks like this:
![iot Rule](/iotRule.png)

## AWS SQS

### Use case

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. Using SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available.

#### To create an SQS queue follow this tutorial: [How to Create an SQS Queue Using the AWS Console](https://www.dummies.com/programming/cloud-computing/amazon-web-services/create-sqs-queue-using-aws-console/)

The body of the message should looks like this:

![iot Rule](/sqsMessage.png)
