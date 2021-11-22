from re import A
import cv2
import numpy as np
from PIL import Image
from keras import models
import tensorflow as tf
from emoji import emojize
#### Defining variables
path = 'trained_models/10classes'
model = models.load_model(path + '/keras_model.h5')
video = cv2.VideoCapture(0)
matrix = np.zeros([1,9])

#### 
def generateLabelList(path):
    label_dictionary = {}
    a_file = open(path + '/labels.txt')
    for line in a_file:
        key, value = line.split()
        label_dictionary[key] = value


    labels = list(label_dictionary.values())
    return labels


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
        labels = generateLabelList('trained_models/10classes') #['mobile_phone', 'keyboard','chair','grinning_face','pencil','closed_book','thumbs_up','eye','balloon']
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
                print(emojize('":' + emoj +':"', use_aliases=True)) #Finds the index of the higest average confidence class and pass that and print the corresponding index of label 
                average = np.zeros([1,9])


video.release()
cv2.destroyAllWindows()




