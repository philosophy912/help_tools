# -*- coding:utf-8 -*-
# --------------------------------------------------------
# Copyright (C), 2016-2020, lizhe, All rights reserved
# --------------------------------------------------------
# @Name:        t2.py
# @Author:      lizhe
# @Created:     2023/6/14 - 13:12
# --------------------------------------------------------
import os
from time import sleep

import pyautogui


def operation_file(input_file: str, output_file: str):
    os.system(f"start {input_file}")
    sleep(5)
    pyautogui.hotkey('ctrl', 'a')
    sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    sleep(1)
    # 关闭区域为2531-24
    #  关闭窗口
    pyautogui.hotkey("alt", "f4")
    sleep(1)
    pyautogui.hotkey('ctrl', 'y')
    sleep(1)
    # pyautogui.click(1343, 775)
    os.system(f"start {output_file}")
    sleep(3)
    # 粘贴
    pyautogui.hotkey('ctrl', 'v')
    # sleep(1)
    # pyautogui.hotkey("win", "up")
    sleep(1)
    pyautogui.hotkey('ctrl', 's')
    sleep(1)
    # pyautogui.typewrite(f"{abs_file_name}.txt")
    # 模拟按下回车键
    # pyautogui.press('enter')
    # sleep(1)
    # pyautogui.hotkey('ctrl', 'y')
    # sleep(1)
    #  关闭窗口
    pyautogui.hotkey("alt", "f4")
    sleep(1)


#
folder = r"D:\Workspace\github\help_tools\El PAIS"
output_folder = r"C:\Users\lizhe\Desktop\rtf_out"

for file in os.listdir(folder):
    directory, file_name = os.path.split(file)
    abs_file_name = file_name.split(".")[0]
    output_f = os.path.join(output_folder, f"{abs_file_name}.txt")
    input_f = os.path.join(folder, file)
    # os.system(f"echo. > {abs_file}")
    print(f"handle file: {input_f}")
    operation_file(input_f, output_f)

# operation_file(r"C:\Users\lizhe\Desktop\rtf\001.rtf", r"C:\Users\lizhe\Desktop\rtf_out\001.txt")
