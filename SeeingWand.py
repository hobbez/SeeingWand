#!/usr/bin/python
import picamera, httplib, urllib, base64, json, re
from os import system
from gpiozero import Button

# CHANGE {MS_API_KEY} BELOW WITH YOUR MICROSOFT VISION API KEY
ms_api_key = "{MS_API_KEY}"

# camera button - this is the BCM number, not the pin number
camera_button = Button(27)

# setup camera
camera = picamera.PiCamera()

# setup vision API
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': ms_api_key,
}

params = urllib.urlencode({
    'visualFeatures': 'Description',
})

# loop forever waiting for button press
while True:
    camera_button.wait_for_press()
    camera.capture('/tmp/image.jpg')

    body = open('/tmp/image.jpg', "rb").read()

    try:
        conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/analyze?%s"%params, body, headers)
        response = conn.getresponse()
        analysis=json.loads(response.read())
        image_caption = analysis["description"]["captions"][0]["text"].capitalize()
	# validate text before system() call; use subprocess in next version
        if re.match("^[a-zA-z ]+$", image_caption):
            system('espeak -ven+f3 -k5 -s120 "' + image_caption + '"')
        else :
            system('espeak -ven+f3 -k5 -s120 "i do not know what i just saw"')

        conn.close()

    except Exception as e:
        print e.args

