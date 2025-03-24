from flask import Flask, render_template, request, redirect, url_for
import cv2 as cv
import numpy as np
from skimage import io
import os

app = Flask(__name__)

# Directorio para guardar las imágenes subidas
UPLOAD_FOLDER = 'images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ruta principal que renderiza el formulario de login
@app.route('/')
def home():
    return render_template('login.html')

# Ruta para procesar la imagen después del login
@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # Obtener la ruta de la imagen desde el formulario
        image_path = request.form['ruta']
        
        # Procesar la imagen
        img1 = io.imread(image_path)
        img1 = cv.cvtColor(img1, cv.COLOR_RGB2BGR)

        # Crear el detector SIFT
        sift = cv.xfeatures2d.SIFT_create()
        kp1, descriptor1 = sift.detectAndCompute(img1, None)

        # Crear una copia de la imagen para dibujar los círculos rellenos
        img1_with_filled_circles = img1.copy()

        # Definir el color y la transparencia
        circle_color = (0, 255, 0)  # Verde
        alpha = 0.3  # Transparencia

        # Dibujar círculos rellenos
        for kp in kp1:
            x, y = int(kp.pt[0]), int(kp.pt[1])
            radius = int(kp.size / 2)
            overlay = img1_with_filled_circles.copy()
            cv.circle(overlay, (x, y), radius, circle_color, -1)
            cv.addWeighted(overlay, alpha, img1_with_filled_circles, 1 - alpha, 0, img1_with_filled_circles)

        # Guardar la imagen procesada
        processed_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'processed_image.jpg')
        cv.imwrite(processed_image_path, img1_with_filled_circles)

        # Redirigir al usuario para mostrar la imagen procesada
        return render_template('index.html', image_url=processed_image_path)
    return render_template('index.html')

# Ejecutar el servidor Flask
if __name__ == '__main__':
    app.run(debug=True)

