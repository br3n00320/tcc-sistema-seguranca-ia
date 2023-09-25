import cv2

# Substitua a URL pela URL RTSP da sua câmera
camera_url = 'rtsp://admin:senha@123456789@192.168.1.15:554/cam/realmonitor?channel=1&subtype=0'

cap = cv2.VideoCapture(camera_url)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Câmera IP', frame)
    
    # Verifique se o usuário pressionou a tecla 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()