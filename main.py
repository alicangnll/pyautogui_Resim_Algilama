import pyautogui, time

def goruntu_tanilama(file, loop):
    start = pyautogui.locateOnScreen(file)
    pyautogui.moveTo(start)
    pyautogui.click(button='left')
    time.sleep(loop)

while(True):
    goruntu_tanilama('./num_9.png', 4)