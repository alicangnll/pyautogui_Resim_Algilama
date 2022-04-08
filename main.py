import pyautogui, time

def goruntu_tanilama(file, loop):
    start = pyautogui.locateOnScreen(file) # İmajı işleyip ekranımızda seçiyoruz
    pyautogui.moveTo(start) # Ekranımızda bulunan konuma mausumuzu otomatik götürüyoruz
    pyautogui.click(button='left') # Sol tık yaptırıyoruz
    time.sleep(loop) # x saniye kadar mola

while(True):
    goruntu_tanilama('./num_9.png', 4) # Sürekli dönen tanıma işlemi 
