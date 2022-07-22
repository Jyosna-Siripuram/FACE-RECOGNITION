
import cv2
from cv2 import FONT_HERSHEY_SIMPLEX
from cv2 import FONT_HERSHEY_DUPLEX
import numpy as np
import os

#plebibsrhnhsfcki

features=np.array[np.array(
    [
        [96,97, 87, ..., 25, 16, 11],
        [96, 96, 86, ..., 23, 15, 13],
        [95, 95, 89, ..., 19, 17, 23],
        ...,
        [29, 30, 12, ...,  6,  7, 17],
        [22, 27, 18, ...,  2,  3, 10],
        [22, 31, 19, ...,  1,  2, 10]],dtype=object),

 np.array([
        [134, 131,  98, ..., 146, 150, 161],
        [127,  95,  44, ..., 143, 143, 147],
        [ 90,  65,  58, ..., 143, 143, 142],
        ...,
        [116, 147, 145, ..., 168, 169, 170],
        [ 73,  67, 117, ..., 170, 171, 169],
        [ 42,  14,  64, ..., 169, 170, 169]],dtype=object),

 np.array([
        [ 30,  23,  27, ...,  16,  14,  14],
        [ 26,  29,  19, ...,  16,  14,  14],
        [ 27,  50,  28, ...,  16,  14,  14],
        ...,
        [217, 209, 214, ...,  24,  29,  32],
        [209, 211, 216, ...,  24,  30,  32],
        [201, 212, 213, ...,  24,  30,  33]]
        ,dtype=object)]



def fr():
    people = []
    for i in os.listdir(r'C:\Users\RamyaJyosna\Desktop\fr\data\training data'):
        people.append(i)
# print(people)
# features = np.load('features.npy',allow_pickle=True)
# labels = np.load('labels.npy')

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read("face_trained.yml")

    image = cv2.imread(r"C:\Users\RamyaJyosna\Desktop\fr\data\training data\musk\elon musk.jpg")
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    if gray.shape>(1000,1000):
        resized_img=cv2.resize(gray,(400,400))
    else:
        resized_img=gray
    print(gray.shape)

    haar_cascade = cv2.CascadeClassifier('haar.xml')
    face_rects = haar_cascade.detectMultiScale(resized_img,scaleFactor =1.5,minNeighbors = 2)

    for (x,y,w,h) in face_rects:
        faces_roi = resized_img[y:y+h,x:x+w]

        label,accuracy = face_recognizer.predict(faces_roi)
       #print(f'Label = {people[label]} , accuracy = {accuracy}')

        cv2.rectangle(resized_img,(x,y),(x+w,y+h),(255,0,0),thickness=2)
       

        if  (features)<=(faces_roi) :
            cv2.putText(resized_img,str(people[label]),(x+3,y+3),FONT_HERSHEY_SIMPLEX,1.2,(0,255,0),thickness=2)
        else:
            cv2.putText(resized_img,str('unknown'),(x+3,y+3),FONT_HERSHEY_DUPLEX,1.2,(0,255,0),thickness=1)

        print('faces_roi:', faces_roi)
        print('features:',features)
        
        #cv2.putText(image,str(people[label]),(x+3,y+3),FONT_HERSHEY_SIMPLEX,1.2,(0,255,0),thickness=2)
        #cv2.putText(image,str('unknown'),(x+3,y+3),FONT_HERSHEY_SIMPLEX,1.2,(0,255,0),thickness=2)
        
        cv2.imshow('detected face',resized_img)
        cv2.waitKey(0)

fr()




