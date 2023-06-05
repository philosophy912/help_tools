# -*- coding:utf-8 -*-
# --------------------------------------------------------
# Copyright (C), 2016-2021, lizhe, All rights reserved
# --------------------------------------------------------
# @Name:        txt_jieba.py
# @Author:      lizhe
# @Created:     2023/4/5 - 21:25
# --------------------------------------------------------
import os.path
import sys

# from time import sleep
# import win32api
# import win32con
try:
    import jieba
except ModuleNotFoundError:
    os.system("pip install jieba")
finally:
    import jieba
# import win32gui

# jieba.enable_paddle()

file = "origin.txt"
output_file = "target.txt"
# 分隔符
spilt_char = " "
result_contents = []

if not os.path.exists(file):
    # hwnd = win32gui.FindWindow((0, ""))
    # 1． 警告信息框
    # result = win32api.MessageBox(1, f"请检查当前文件夹下面是否存在[{file}]文件", "警告", win32con.MB_OK)
    print(f"请检查当前文件夹下面是否存在[{file}]文件")
    # sleep(1)
    sys.exit(1)
if os.path.exists(output_file):
    try:
        os.remove(output_file)
    except OSError:
        print(f"请关闭{output_file}再试")
        # sleep(1)
        sys.exit(1)

print(f"正在分割{file}中的词条, 请耐心等待")
with open(file, "r", encoding="utf-8") as f:
    contents = f.readlines()
    for line in contents:
        line = line.replace("\n", "")
        result_content = jieba.cut(line)
        result_line = spilt_char.join(result_content)
        result_contents.append(result_line)
print(f"正在将分割词条写入{output_file}中,请耐心等待")
with open(output_file, "w", encoding="utf-8") as f:
    for result_line in result_contents:
        f.write(f"{result_line}\n")
print(f"分词完成，请查看文件[{output_file}]")
