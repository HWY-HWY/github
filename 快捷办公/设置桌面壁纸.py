"""
设置桌面壁纸
"""

import win32api
import win32con
import win32gui


def setwallpaper(path):
    # 打开注册表
    win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 设置壁纸路径
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)


path = r"C:\Users\Administrator\Desktop\个人博客\壁纸.jpg"
setwallpaper(path)
