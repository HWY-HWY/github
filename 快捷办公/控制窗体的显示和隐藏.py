import win32con
import win32gui
import time

while True:
    winQQ = win32gui.FindWindow("TXGuiFoundation", "QQ")
    win32gui.ShowWindow(winQQ, win32con.SW_SHOW)
    time.sleep(1)
    win32gui.ShowWindow(winQQ, win32con.SW_HIDE)
    time.sleep(1)
