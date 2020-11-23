# Note : this code was written for educational perposes only
# you have to install "pyautogui" using  this command  :
# pip install pyautogui

# importing part 
import pyautogui
import time
# main part
count = 0
pyautogui.click(10,5)
# do for ever :)
while True :

    # creating a kill switch
    pyautogui.FAILSAFE = True
    # kill switch is putting the mouse cursor in the top left corner of screen :)

    # you can write your favorite massage here 
    pyautogui.write(f"spam bot test")

    count = 1  
    # send massage 
    pyautogui.press("ENTER")
    # wait for site to response 
    time.sleep(1)
# go to https://web.whatsapp.com/ or your sightly messenger web version or app select the chat and run this code 
# make sure that you set the messenger to send massage by hitting Enter
