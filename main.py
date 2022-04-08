import pyautogui, time, sys
from python_imagesearch.imagesearch import imagesearch

def goruntu_isleme_opencv(file, cooldown):
    pos = imagesearch(file)
    if pos[0] != -1:
        pyautogui.moveTo(pos[0], pos[1]) # move mouse to image
        pyautogui.click(button='left') # Left click
        print(pos) # print position
        time.sleep(cooldown) # cooldown
    else:
        print("image not found") # image not found

try:
    while(True):
        goruntu_isleme_opencv('./num_9.png', 2)
except goruntu_isleme_opencv:
    sys.exit(1)
