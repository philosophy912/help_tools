# -*- coding:utf-8 -*-
# --------------------------------------------------------
# Copyright (C), 2016-2020, omosoft, All rights reserved
# --------------------------------------------------------
# @Name:        t7.py
# @Author:      lizhe
# @Created:     2024/10/4 - 23:12
# --------------------------------------------------------
from stanfordcorenlp import StanfordCoreNLP

file = r"d:\《习近平谈治国理政 第三卷》.txt"
file1 = r"d:\2.txt"
# with open(file1, "r",encoding="utf-8") as f:
#     contents = f.readlines()
#     for content in contents:
#         print(content)
#         result = nlp.pos_tag(content)
#         print(result)

#默认是英文
with StanfordCoreNLP(r'D:\Tools\stanford-corenlp-4.5.7', lang='zh') as nlp:
    result = nlp.pos_tag("某一个词的前后是动词还是名词")
    # result = nlp.pos_tag("i am a teacher")
    print(result)
