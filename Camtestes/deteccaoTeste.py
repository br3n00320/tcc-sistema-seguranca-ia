import cv2

# Parâmetros de acesso da câmera
USERNAME = 'admin'
PASSWORD = 'senha@123456789'
IP = '192.168.1.15'
PORT = '554'

# URL da câmera stream
URL = 'rtsp://{}:{}@{}:{}/cam/realmonitor?channel=1&subtype=0'.format(USERNAME, PASSWORD, IP, PORT)

# Inicializa o classificador Haar Cascade para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicia a captura de vídeo
cap = cv2.VideoCapture(URL, cv2.CAP_FFMPEG)

# resolução 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Largura 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Altura 

while True:
    ret, frame = cap.read()
    if ret == False:
        print("Sem frame")
        break
    else:
        # Converte o frame para tons de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detecta rostos no frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Desenha um retângulo ao redor de cada rosto detectado
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('VIDEO', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
