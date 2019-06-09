import numpy 
import cv2
import socket
import json
import base64

# Read image
img = cv2.imread('lena_gray.bmp',0)
cv2.imshow('image',img)

with open("lena_gray.bmp", "rb") as f:
    jpg = f.read()

#conn
serverName = '175.113.152.102'
serverPort = 17171
print("Connecting :", serverName, serverPort)
device = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device.connect((serverName, serverPort))

#send
data = {}
strarr = numpy.array_str(img)
#print("string", strarr)
strb64 = base64.b64encode(strarr.encode()).decode()
#print("base64", strb64)
strarr = base64.b64decode(strb64)

data['img'] = base64.b64encode(jpg).decode()
data['txt'] = "from macbook with love"
jsondata = json.dumps(data)

print("LENG", len(jsondata))
print("DATA", jsondata.encode())
device.send(('%d\n' % len(jsondata)).encode())
device.sendall(jsondata.encode())
device.send(('%d\n' % len(jsondata)).encode())
device.sendall(jsondata.encode())


k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
