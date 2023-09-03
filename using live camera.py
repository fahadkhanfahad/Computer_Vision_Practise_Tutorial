# 1-initialize video capture object
# 2-read frame by frame
# 3-if status true continue loop or else break
# 4-release the frame


    
import cv2

capture=cv2.VideoCapture(0)

while(True):
    status,frame=capture.read()
    if not status:
        break
    #now you can perfrom any operation but curretly i am shoing simple image
    cv2.imshow("Live Cam",frame)
     #now grayscale
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    cv2.imshow("Gray Image",frame)

    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()    

