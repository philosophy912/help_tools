# -*- coding:utf-8 -*-
# --------------------------------------------------------
# Copyright (C), 2016-2020, omosoft, All rights reserved
# --------------------------------------------------------
# @Name:        group_and_split.py
# @Author:      lizhe
# @Created:     2024/11/4 - 16:55
# --------------------------------------------------------
import os
import jieba

folder = r"C:\Users\lizhe\Desktop\欧华报编译新闻的文本文档"
output = "result.txt"
files = [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith("txt")]
contents = []

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            results = jieba.cut(line)
            contents.append(" ".join(results))

contents = [line for line in contents if line.replace("\n", "") != ""]
with open(output, "w", encoding="utf-8") as f:
    for line in contents:
        f.write(f"{line}\n")
