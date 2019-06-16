import io
import numpy as np
import cv2
import socket
import json
import base64
from PIL import Image

def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    image = Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

#conn
serverName = '175.113.152.102'
serverPort = 17171
print("Connecting :", serverName, serverPort)
device = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device.connect((serverName, serverPort))

# Read video
cap = cv2.VideoCapture("squat1.mp4")

#send
data = {}
skip = 10
fno = 0
if cap.isOpened() is False:
    print("Error opening video stream or file")
while cap.isOpened():
    ret_val, image = cap.read()
    if fno == 10:
        ret_bmp, bmp = cv2.imencode(".bmp", image)
        # Into JSON
        data['img'] = base64.b64encode(bmp).decode()
        data['txt'] = "from macbook with love"
        jsondata = json.dumps(data)
        # Sending to server (which will forward to client)
        device.send(('%d\n' % len(jsondata)).encode())
        device.sendall(jsondata.encode())
        # For debug
        print("LENG", len(jsondata))
        #print("DATA", jsondata.encode())
        cv2.imshow('Sent image (original)', image) 
        cv2.imshow('Sent image (decoded in python)', stringToRGB(data['img']))
    if cv2.waitKey(1) == 27:
        break
    fno += 1

cv2.destroyAllWindows()
