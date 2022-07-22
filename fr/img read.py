import cv2
import os
import face_recognition 

# cam = cv2.VideoCapture(0)
# # reading the input using the camera
# result, image = cam.read()
  
# # If image will detected without any error, 
# # show result
# if result:
#     # saving image in local storage
#     cv2.imwrite("img1.jpg", image)
  
#     # If keyboard interrupt occurs, destroy image 
#     # window
#     cv2.waitKey(0)
#     cv2.destroyWindow("img1")
  
# # If captured image is corrupted, moving to else part
# else:
# print("No image detected. Please! try again")

#-----------------way1-----------#

cam = cv2.VideoCapture(0)
#i=0
while True:

     
     isTrue,frame = cam.read()
     cv2.imshow('Video',frame)
#    cv2.imwrite('frame'+str(i)+'.jpg',frame)
     face_recognition.fr()

#      i+=1
     if cv2.waitKey(0) & 0xFF==ord('d'):
        break
     
cam.release()
cv2.destroyAllWindows()

#-------------------way2---------------------

# storing the live video as mp file and detecting faces
# cam = cv2.VideoCapture('')

# try:
      
#     # creating a folder named data
#     if not os.path.exists('data'):
#         os.makedirs('data')
  
# # if not created then raise error
# except OSError:
#     print ('Error: Creating directory of data')

# currentframe = 0
  
# while(True):
      
#     # reading from frame
#     ret,frame = cam.read()
  
#     if ret:
#         # if video is still left continue creating images
#         name = './data/frame' + str(currentframe) + '.jpg'
#         print ('Creating...' + name)
  
#         # writing the extracted images
#         cv2.imwrite(name, frame)
  
#         # increasing counter so that it will
#         # show how many frames are created
#         currentframe += 1
#     else:
#         break
  
# # Release all space and windows once done
# cam.release()
# cv2.destroyAllWindows()
