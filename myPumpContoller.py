'''
So this is a device which controls the pump
First I created a thing called pump controller
Then got all the certificates for the same....

Lets start
28-October-2017

Lets put it in git as well

Awesome... git repository created as well...


Shadow JSON schema:

"state": {
    "reported":{
#			"pump_state":<value>
#		}
#	}
'''

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import argparse

#We get the initialise state via argument
# Read in command-line parameters
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--value", action="store", required=True, dest="initValue", help="Enter the initialise value")

initValue = args.initValue

#Credentials
#Root Certificate
rootCAPath = "./root-CA.crt"
#Private Key
privateKeyPath = './roomTemperature.private.key'
#certificate
certificatePath = './roomTemperature.cert.pem'
#Host: This is where your thing is present
host = 'a2wp40g71pc111.iot.eu-west-2.amazonaws.com'
#I guess this is the thing name
clientId = 'pump',
#Not sure where region is used
region = 'eu-west-2'

#My callbacks defined here
def deltaHanldlerCallback(payload, responseStatus, token)
    print "Do Something for delta changes"
    
#Call back for update
def updateHanldlerCallback(payload, responseStatus, token)
    print "Do Something for Update callback"



# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

#Initialise the client
myAWSIoTMQTTShadowClient = None
myAWSIoTMQTTShadowClient = AWSIoTMQTTShadowClient(clientId)
myAWSIoTMQTTShadowClient.configureEndpoint(host, 8883)
myAWSIoTMQTTShadowClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTShadowClient configuration
myAWSIoTMQTTShadowClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTShadowClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTShadowClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect to AWS IoT
myAWSIoTMQTTShadowClient.connect()

# Create a deviceShadow with persistent subscription
deviceShadowHandler = myAWSIoTMQTTShadowClient.createShadowHandlerWithName(clientId, True)

# Listen on deltas
deviceShadowHandler.shadowRegisterDeltaCallback(deltaHanldlerCallback)

#Update callback added
myDeviceShadow.shadowUpdate(myJSONPayload, updateHanldlerCallback, 5)




