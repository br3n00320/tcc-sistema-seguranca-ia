import cv2
import os

#parametros de acesso da camera
USERNAME = 'admin'
PASSWORD = 'senha@123456789'
IP = '192.168.1.15'
PORT = '554'

#so roda se for ffmpeg
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

#url da camera stream varia conforme o modelo da camera
URL = 'rtsp://{}:{}@{}:{}/cam/realmonitor?channel=1&subtype=0'.format(USERNAME, PASSWORD, IP, PORT)

path_cascade = "haarcascade_frontalface_alt2.xml"
# defining face detector
face_cascade=cv2.CascadeClassifier(path_cascade)
ds_factor=0.6
class VideoCamera(object):
    def __init__(self):
       #capturing video
       #self.video = cv2.VideoCapture(0)
       self.video = cv2.VideoCapture(URL, cv2.CAP_FFMPEG)
       #self.fgbg = cv2.createBackgroundSubtractorKNN()
    
    def __del__(self):
        #releasing camera
        self.video.release()
    
    def get_frame(self):
       #extracting frames
        ret, frame = self.video.read()

        #fgmask = self.fgbg.apply(frame)

        frame=cv2.resize(frame,None,fx=ds_factor,fy=ds_factor,interpolation=cv2.INTER_AREA)                    
        
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        face_rects=face_cascade.detectMultiScale(gray,1.3,5)
        
        for (x,y,w,h) in face_rects:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            break
        #encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()