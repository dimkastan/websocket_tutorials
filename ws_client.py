""""
Author: Dimitris Kastaniotis

https://github.com/dimkastan


"""
import asyncio
import websockets
import cv2
import numpy as np
from io import BytesIO

import argparse

parser = argparse.ArgumentParser(description='Receive and display image from a remote end point over websockets')
parser.add_argument('--server_address', type=str,  default="localhost" ,  help='target server address')
parser.add_argument('--server_port', type=int,   default=8765,  help='target server port')

args = parser.parse_args()

PORT    = args.server_port
ADDRESS = args.server_address

print("Server address: {} \nServer port: {}".format(ADDRESS, PORT))
async def receiver(ip="localhost", port=8765):
    uri = "ws://"+ip + ":" + str(port)
    async with websockets.connect(uri) as websocket:
        while(1):
          binary_data = await websocket.recv()
          bdata = BytesIO(binary_data)
          loaded_np = np.load(bdata )
          rim= cv2.imdecode(loaded_np,1) 
          cv2.imshow("image", rim)
          key= cv2.waitKey(10)

asyncio.get_event_loop().run_until_complete(receiver(ADDRESS, PORT))