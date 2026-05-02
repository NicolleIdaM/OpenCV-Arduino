import cv2
import serial
import time

port = 'COM3'

try:
    arduino = serial.Serial(port, 9600, timeout=1)
    time.sleep(2)
    print("Conected With Arduino")
except:
    print(f"Error: not being connected to port {port}")
    exit()
    
face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Error opening camera")
    exit()

print("Press 'e' to exit")
    
while True:
    ret, frame = webcam.read()
    
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(faces) > 0:
        for (x, y, l, a) in faces:
            cv2.rectangle(frame, (x, y), (x+l, y+a), (0, 255, 0), 2)
            
            cv2.putText(frame, "Frame detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            arduino.write(b'1')
    else:
        cv2.putText(frame, "Frame undetected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        arduino.write(b'0')
        
    cv2.imshow('OpenCv + Arduno', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
        
webcam.release()
cv2.destroyAllWindows()
arduino.close()
print("Program closed")