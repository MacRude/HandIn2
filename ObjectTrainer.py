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
        img_array = (img_array.astype(np.float32) / 127.0) - 1

        #Calling the predict function using keras
        prediction = model.predict(img_array)
        print(prediction)
        labels = ['Phone', 'Keyboard','Chair','Happy face','Pen','Book','Thumbs up','Eye','Balloon']
        print(labels[np.argmax(prediction)])
        idx = np.argmax(prediction) ## argmax returns the value of the label with the highest confifence
        print(labels[idx])
        cv2.imshow("Prediction", frame)
        key=cv2.waitKey(1)
        if key == ord('q'):
                break
        
video.release()
cv2.destroyAllWindows()