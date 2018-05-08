import pygame
import time


# 指定路径
path1 = r"E:\CloudMusic\阿桑 - 一直很安静.mp3"
path2 = r"E:\CloudMusic\GALA - 追梦赤子心.mp3"

# 初始化
pygame.mixer.init()
# 加载音乐
music = pygame.mixer.music.load(path1)
# 播放音乐
pygame.mixer.music.play()
time.sleep(10)
# 设置下一首播放的音乐
music = pygame.mixer.music.load(path2)
pygame.mixer.music.play()
# 延时，让程序循环执行，就能一直播放音乐
time.sleep(20)
# 停止播放
pygame.mixer.music.stop()
