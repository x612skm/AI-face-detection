import cv2
from random import randrange
trained_face_data = cv2.CascadeClassifier('harcascade_face.xml')

#img = cv2.imread('srk_image.jpg')
#grayscale image
webcam = cv2.VideoCapture(0)
while True:
    #read the current frame
    successful_frame_read, frame = webcam.read()
    grayscaled_img=cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)

#detect facse
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
#print(face_coordinates)

#draw rectange over the faces
#loopoing through all the human beings in the loop
    for(x,y,w,h) in face_coordinates: #it will make sense as a corrdinates in array
        cv2.rectangle(frame, (x,y), (x+w, y+h), (randrange(226),randrange(226),randrange(226)), 2)
#randrange is the function so that separetly identify all the faces





    cv2.imshow('hello ', frame)
    key = cv2.waitKey(1)
    ### stop if Q key is pressed
    if key==81 or key==113: #ascii value of Q key
        break
    print("code complete")
webcam.release()
