import webbrowser 
import pyautogui
import time 

def open_browser():
    webbrowser.open('http://facebook.com')
    time.sleep(7)
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    screenshot.show()

open_browser()

    
    