"""
用程序模拟按键盘
"""

import win32api
import win32con
import time

# # 按下键盘
# win32api.keybd_event(91, 0, 0, 0)
# time.sleep(0.1)
# # 抬起按键
# win32api.keybd_event(91, 0, win32con.KEYEVENTF_KEYUP, 0)

while True:
    win32api.keybd_event(91, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(68, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(91, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(4)
