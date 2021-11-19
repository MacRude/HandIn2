import cv2
import numpy as np
from PIL import Image
from keras import models
import tensorflow as tf
import os

cwd = os.getcwd() 
model = models.load_model(cwd + '/trained_models/10classes/keras_model.h5')
video = cv2.VideoCapture(0)

while True:
        _, frame = video.read()
        #Convert the captured frame into RGB
        im = Image.fromarray(frame, 'RGB')

        #Resizing into dimensions you used while training
        im = im.resize((224,224))
        img_array = np.array(im)
        img_array = np.expand_dims(img_array, axis=0)

        #Calling the predict function using keras
        prediction = model.predict(img_array)
        labels = ['phone', 'water bottle']
        print(np.argmax(prediction)) # get index of max
        print(labels[np.argmax(prediction)])

        cv2.imshow("Prediction", frame)
        key=cv2.waitKey(1)
        if key == ord('q'):
                break
video.release()
cv2.destroyAllWindows()