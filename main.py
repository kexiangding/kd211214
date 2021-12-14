# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#why import cause run the file?
#How to step by step debug?
#How to use the opencv?
#How to use Cuda? GPU, Install CUDA
#How to use matlab?
import ImgSegment
#from ImgSegment import PI

#def calc_round_area(radius):
#    return ImgSegment.PI*(radius**2)
# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print('round area:', calc_round_area(1))
#    ImgSegment.print_hi('PyCharm')

# Python program to read image using OpenCV

# importing OpenCV(cv2) module
import cv2 #`1

# Save image in set directory
# Read RGB image
img = cv2.imread('C:/kd/Test1.png')
#print type(img)
# Output img with window name as 'image'
cv2.imshow('image', img)

# Maintain output window utill
# user presses a key
cv2.waitKey(0)

# Destroying present windows on screen
cv2.destroyAllWindows()