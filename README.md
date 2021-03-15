@@ -1 +1,24 @@
# prototype-captcha-cracker

GUI:
Creates a gui which mimics the functionality of a reCaptcha. Displays 3 fire hydrants mixed with 6 other random images.
When the three fire hydrants, and nothing else, have been clicked, the website is unlocked. 

Captcha Cracker:
Takes a screenshot and identifies the keypoints. Loops through the fire hydrant database, identifies the keypoints of each of the images, then attempts to match them to the screenshot keypoints. If the matches meet a minimum requirement, it means that there is a fire hydrant on the screen. It will find the average coordinates of the keypoints and click on that point. This will click on the fire hydrants within the reCaptcha.

To use:
-Ensure the working directory contains the database folder so python can find the images
-Install all the required libraries, as specified in REQUIREMENTS.txt
-Run captcha_gui.py and ensure it is visible on screen
-Run captcha_cracker.py and let it run through. Once it is finished, click verify on reCaptcha 




To do for gui:
    -Better graphics for unlocked 'website'
    -"Please try again" graphics
    -Visual effects when image has been pressed. (Shrinking and tick in top left corner)

To do for catpha cracker:
    -Automatically click on verify button when fire hydrants have been clicked
