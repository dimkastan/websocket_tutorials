# Web socket tutorial series 

Author:

Dimitris Kastaniotis

https://github.com/dimkastan

### Python to python communication

- About

This example demonstrates the transmition of image data over WebSockets.
Image is first PNG compressed and send as binary.
It is tested on Windows and Ubuntu OS.

- Dependencies
OpenCV python bindings

```
pip install opencv-python
```


- How to run

ASsuming that you have one USB camera mounted on your PC
- First start the server

```
python ws_server.py --source camera --camera 0
```

- Then run the client

```
python ws_client.py
```




