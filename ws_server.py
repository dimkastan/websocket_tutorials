"""

Author: Dimitris Kastaniotis

https://github.com/dimkastan


"""
import asyncio
import websockets
import datetime
import random
import cv2
import numpy as np
from io import BytesIO
import datetime
import random
import argparse

parser = argparse.ArgumentParser(description='Send image to a remote end point over websockets')
parser.add_argument('--filename', type=str,     help='image filename')
parser.add_argument('--video', type=str,     help='video filename')
parser.add_argument('--camera', type=int,     help='camera ID')
parser.add_argument('--server_address', type=str,  default="localhost" ,  help='target server address')
parser.add_argument('--server_port', type=int,   default=8765,  help='target server port')
parser.add_argument("--source",  type=str,  choices=["video", "camera"])

args = parser.parse_args()
print(args)
PORT    = args.server_port
ADDRESS = args.server_address
filename = args.filename
video = args.video
camera = args.camera
source = args.source
videosource = None
if(source=="video"):
    if(video==None):
        print("Video source requires a video fileto be defined")
    else:
        videosource=video
elif(source=="camera"):
    if(camera==None):
        print("Video source requires a video fileto be defined") 
    else:
        videosource=camera


async def video(websocket, path):
    while cap.isOpened():
        status, image = cap.read()
        if(status):
            status, data=cv2.imencode('.PNG',image)
            now = datetime.datetime.utcnow().isoformat() + "Z"
            np_bytes = BytesIO()
            np.save(np_bytes, data, allow_pickle=True)
            binary_data = np_bytes.getvalue()
            await websocket.send(binary_data )

if __name__=="__main__":
    print("Openinng: {}".format(videosource))
    cap = cv2.VideoCapture(videosource)
    start_server = websockets.serve(video, ADDRESS, PORT)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()