import cv2
import numpy as np
import pyautogui
import os

sift = cv2.xfeatures2d.SIFT_create()
FLANN = cv2.FlannBasedMatcher(dict(algorithm=0, trees=5), dict(checks=50))


def get_keypoints(img):

    kpts = sift.detect(img, None)
    desc = sift.compute(img, kpts)

    return kpts, desc


# Compares the two keypoints and determines whether it meets the minimum number of matches
def compare_images(desc1, desc2, minm_matches=35):
    kp_matches = FLANN.knnMatch(desc1[1], desc2[1], 2)
    matchesMask = [[0,0] for i in range(len(kp_matches))]

    # Good keypoint matches are stored in a list
    good_matches = []
    for x,y in kp_matches:
        if x.distance < 0.5*y.distance:
            good_matches.append(x)


    return (len(good_matches) > minm_matches), good_matches


def click(img, screenshot):
    #Computes the keypoints and the descriptors of both inputted images
    kpts1, descs1 = sift.detectAndCompute(img, None)
    kpts2, descs2 = sift.detectAndCompute(screenshot, None)

    captchaPoints = []

    #Compares the keypoints and the descriptors and store the good matches in a list
    matches = FLANN.knnMatch(descs1, descs2, 2)
    matchesMask = [[0,0] for i in range(len(matches))]
    
    for i, (m1,m2) in enumerate(matches):
        if m1.distance < 0.7 * m2.distance:
            matchesMask[i] = [1,0]
            pts = kpts2[m1.trainIdx].pt

            captchaPoints.append(pts)


    x_values = [i[0] for i in captchaPoints]
    y_values = [i[1] for i in captchaPoints]


    x_mean = np.mean(x_values)
    y_mean = np.mean(y_values)

    pyautogui.click(x_mean, y_mean)

    return True



def main():
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2GRAY)
    cv2.imwrite("screenshot.png", screenshot)
    
    screenkp, screendesc = get_keypoints(screenshot)

    direc = "database/hydrants/"

    for f in os.listdir(direc):
        print(direc + f)
        img = cv2.imread(direc + f, 0) 
        imgkp, imgdesc = get_keypoints(img)

        passed, matches = compare_images(screendesc, imgdesc)


        if passed:
            click(img, screenshot)

main()
