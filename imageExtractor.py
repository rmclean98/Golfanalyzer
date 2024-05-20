import cv2 as cv
import numpy as np

videoName = 'rorySwing'
index = 1

cap = cv.VideoCapture(videoName + '.mp4')



while(cap.isOpened()): 
      
# Capture frame-by-frame 
    ret, frame = cap.read() 
    if ret == True: 
        cv.imwrite('Images/Rory/' + videoName + f'_{index}.jpg', frame)
        # Display the resulting frame 
        # cv.imshow('Frame', frame) 
        index += 1
          
    # Press Q on keyboard to exit 
        #if cv.waitKey(25) & 0xFF == ord('q'): 
        #    break
  
# Break the loop 
    else: 
        break
  
# When everything done, release 
# the video capture object 
cap.release() 
  
# Closes all the frames 
cv.destroyAllWindows() 