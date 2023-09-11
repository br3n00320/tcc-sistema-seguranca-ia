import cv2
import os

USERNAME = 'admin'
PASSWORD = 'senha@123456789'
IP = '192.168.1.12'
PORT = '554'

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

URL = 'rtsp://{}:{}@{}:{}/live/mpeg4'.format(USERNAME, PASSWORD, IP, PORT)
print('Conectando com: ' + URL)

cap = cv2.VideoCapture(URL, cv2.CAP_FFMPEG)

while True: 
    ret, frame = cap.read()
    if not ret:
        print("Sem frame")
        break
    else:
        cv2.imshow('VIDEO', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()