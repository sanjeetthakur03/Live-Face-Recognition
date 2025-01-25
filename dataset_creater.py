import sqlite3

import cv2
import numpy as np
import _sqlite3

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');#to detect the face shown in camera
cam = cv2.VideoCapture(0); # 0 for web camera

def insertorupdate(Id, Name, Age):  # function for SQL database
    conn = sqlite3.connect("database.db")
    cmd = "SELECT * FROM STUDENTS WHERE ID = ?"
    cursor = conn.execute(cmd,(Id,))
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if isRecordExist == 1:
        conn.execute("UPDATE STUDENTS SET Name = ? WHERE Id = ?", (Name, Id))
        conn.execute("UPDATE STUDENTS SET Age = ? WHERE Id = ?", (Age, Id))
    else:
        conn.execute("INSERT INTO STUDENTS(Id, Name, Age) VALUES(?, ?, ?)", (Id, Name, Age))

    conn.commit()
    conn.close()

# insert user defined values
Id=input('Enter User Id ')
Name=input('Enter user Name ')
Age=input('Enter User Age ')

insertorupdate(Id,Name,Age)

#detecting face in web camera coding
sampleNum=0; #assume there is no samples in dataset
while(True):
    ret,img=cam.read();  #open camera
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #image convert into bgrGray color
    faces=faceDetect.detectMultiScale(gray,1.3,5) #scale factor
    for(x,y,w,h)in faces:
        sampleNum=sampleNum+1; # if faces detected ,increments sampleNum
        cv2.imwrite("dataset/user."+str(Id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) #create a rectangle on faces
        cv2.waitKey(100) #delay time
    cv2.imshow("Face",img) #show face detected in camera
    cv2.waitKey(1);
    if(sampleNum>20): #if the dataset is >20 break
        break;
cam.release()
cv2.destroyAllWindows() #quit


