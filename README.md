# Convert an image to black and white using python

Requirements :
  1. OpenCV Library - cv2 module
  2. Python - version > 3.7
  
 # OpenCV :
 OpenCV is an open source computer vision and machine learning software library.
 
 # Method used :
 Binary threshold Operation -->
    1. Convert an image to gray scale image and we define a threshold value.
    2. Then, for each pixel of the gray scale image, if its value is lesser than the threshold, then we assign to it the value 0 (black).
    3. Otherwise, we assign to it the value 255 (white).
    
 # Process :
    1. Import cv2 module of openCV library
    2. Obtain the color image and change to grayscale image
    3. Assign threshold value to 127 or 128 (mid value of 0 and 255)
    4. Since, it is binary threshold we use "THRESH_BINARY"  function to convert to black and white
    5. Save your black and white image 
    
 # LEARNING IS FUN
 
 
