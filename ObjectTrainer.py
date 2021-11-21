from re import A
import cv2
import numpy as np
from PIL import Image
from keras import models
import tensorflow as tf
import os
from emoji import emojize

cwd = os.getcwd() 
model = models.load_model(cwd + '/trained_models/10classes/keras_model.h5')
video = cv2.VideoCapture(0)

matrix = np.zeros([1,9])

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
        #print(prediction)
        labels = ['mobile_phone', 'keyboard','chair','grinning_face','pencil','closed_book','thumbs_up','eye','balloon']
        #print(labels[np.argmax(prediction)])
        cv2.imshow("Prediction", frame)
        key=cv2.waitKey(1)
        if key == ord('q'):
                break

        #Numpy array
        matrix = np.vstack((matrix, prediction))
        average = np.average(matrix, axis=0) 
        print(average)   
        if matrix.shape[0] % 30 == 0: #.shape returns a tuple, so access first index of tuple and see if modulo 30 == 0.
                emoj = labels[average.argmax(axis=0)]
                print(emojize('":' + emoj +':"')) #Finds the index of the higest average confidence class and pass that and print the corresponding index of label 
                average = np.zeros([1,9])


video.release()
cv2.destroyAllWindows()




