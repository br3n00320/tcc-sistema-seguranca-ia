import cv2
import dlib
import os
# Inicializa o detector de rostos
detector = dlib.get_frontal_face_detector()

# Carrega o modelo pré-treinado para a detecção facial
predictor = dlib.shape_predictor('/home/lucas/Downloads/videostream-master/shape_predictor_68_face_landmarks.dat')  # Você deve baixar esse modelo

#parametros de acesso da camera
USERNAME = 'admin'
PASSWORD = '123456789LB'
IP = '192.168.1.139'
PORT = '554'

#so roda se for ffmpeg
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

#url da camera stream varia conforme o modelo da camera
URL = 'rtsp://{}:{}@{}:{}/onvif1'.format(USERNAME, PASSWORD, IP, PORT)
print('Conectando com: ' + URL)

cap = cv2.VideoCapture(URL, cv2.CAP_FFMPEG)

# Reduza a resolução desejada
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Largura desejada
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Altura desejada

while True:
    ret, frame = cap.read()
    if ret == False:
        print("Sem frame")
        break
    else:
        # Converte o frame para tons de cinza para a detecção de rosto
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detecta rostos no frame
        faces = detector(gray)

        # Desenha um retângulo ao redor de cada rosto detectado
        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('VIDEO', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
