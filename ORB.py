# -*- coding: utf-8 -*-


import cv2
  
  
# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('cam_test', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

img2=cv2.imread('main.png')
orb=cv2.ORB_create(1000)

kp1, des1=orb.detectAndCompute(frame, None)
kp2, des2=orb.detectAndCompute(img2, None)

for d1 in des1:
    print(d1[:10])
    
for d2 in des2:
    print(d2[:10])

bf=cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)   
#cv2.NORM_HAMMING calculates the Hamming distance between zero and image array.
#https://en.wikipedia.org/wiki/Hamming_distance

#'crossCheck=False' matches every descriptor of test image to all the descriptors of the main image.

matches=bf.match(des1, des2)
print(len(matches))

matches=sorted(matches, key=lambda x:x.distance)

results=cv2.drawMatches(frame, kp1, img2, kp2, matches[:50], None, flags=2)
#selecting top 20 best matches

cv2.imshow('Matching results', results)
cv2.waitKey(0)
cv2.destroyAllWindows()
