import dlib
import cv2

# Inicializa o detector de rostos
detector = dlib.get_frontal_face_detector()

# Carrega o modelo pré-treinado para a predição de landmarks faciais
predictor = dlib.shape_predictor('modelo/shape_predictor_68_face_landmarks.dat')

# Lista para armazenar os landmarks de todas as imagens
landmarks_lista = []

# Processa cada uma das suas 40 fotos
for i in range(1, 44):  # Assumindo que as fotos tenham nomes sequenciais de 1 a 40
    # Carrega a imagem
    imagem = cv2.imread(f'fotos/breno/{i}.jpg')  

    # Converte a imagem para tons de cinza
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Detecta rostos na imagem
    faces = detector(gray)

    # Se um rosto foi detectado
    if len(faces) > 0:
        # Prediz os landmarks faciais para o rosto
        landmarks = predictor(gray, faces[0])  # Vamos assumir que estamos interessados apenas no primeiro rosto

        # Adiciona os landmarks à lista
        landmarks_lista.append(landmarks)

