import cv2
import serial
import time

port = 'COM3'

try:
    arduino = serial.Serial(port, 9600, '1')
    time.sleep(2)
    print("Conected With Arduino")
except:
    print("Error: not being connected to port {port}")
    exit()