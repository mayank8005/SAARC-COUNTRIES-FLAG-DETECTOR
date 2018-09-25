import cv2
import numpy as np
import os

# thinkness of detection window
STROKE = 2
#color of detection window in RGB
COLOR_OF_DETECTION_WINDOW = (255, 0, 0)

#templates
TEMPLATE_INDIA = cv2.resize((cv2.imread('templates/India.png', 0)), (0,0),
                                                    fx=0.9, fy=0.9)

TEMPLATE_SRILANKA = cv2.resize((cv2.imread('templates/Srilanka.png', 0)), (0,0),
                                                    fx=0.9, fy=0.9)


TEMPLATE_BANGLADESH = cv2.resize((cv2.imread('templates/Bangladesh.png', 0)), (0,0),
                                                    fx=0.9, fy=0.9)

TEMPLATE_PAK = cv2.resize((cv2.imread('templates/Pak.png', 0)), (0,0),
                                                    fx=0.9, fy=0.9)

TEMPLATE_BHUTAN = cv2.resize((cv2.imread('templates/Bhutan.png', 0)), (0,0),
                                                    fx=0.9, fy=0.9)

TEMPLATE_AFG = cv2.resize((cv2.imread('templates/Afg.png', 0)), (0,0),
                                                    fx=0.8, fy=0.8)

TEMPLATE_MAL = cv2.resize((cv2.imread('templates/Mal.png', 0)), (0,0),
                                                    fx=0.8, fy=0.8)

# array of templates
templates = [TEMPLATE_INDIA, TEMPLATE_SRILANKA, TEMPLATE_BANGLADESH,
    TEMPLATE_PAK, TEMPLATE_BHUTAN, TEMPLATE_AFG, TEMPLATE_MAL]

# boolean to identify that object is detected
is_detected = False

def detect(test_img):
    """Detects given image have SAARC country's flag or not"""

    global is_detected

    # converting test image in RGB
    test_gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

    #iteration for each template
    for template in templates:

        #extrating width and height of template
        w, h = template.shape[ : :-1]

        # matching template with image
        res = cv2.matchTemplate(test_gray, template, cv2.TM_CCOEFF_NORMED)
        # thershold can be set between 0 to 1
        # it is thershold of allowing match result
        threshold = 0.75
        loc = np.where(res >= threshold)

        # adding rectangle of detection
        for pt in zip(*loc[::-1]):

                is_detected = True
                cv2.rectangle(test_img, pt, (pt[0]+w, pt[1]+h),
                                        COLOR_OF_DETECTION_WINDOW, STROKE)

    # checking if anything is detected of not
    if is_detected is True:
        cv2.imshow('detected', test_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print('SAARC FLAG NOT DETECTED')

# input: path of image to be tested
path = raw_input('enter path of image file to test: ')

if os.path.exists(path):
    test_img = cv2.imread(path)
    detect(test_img)

else:
    print("404\nFILE NOT FOUND")
