# coding=utf-8
from utils.img_compare import compare

import pyautogui

pic_1 = "D:\\Python27\\workspace\\lushi_cheater\\imgs\\mockery.png"
img_location = pyautogui.locateOnScreen(pic_1)
print(img_location)
