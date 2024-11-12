# -*- coding:utf-8 -*-
# --------------------------------------------------------
# Copyright (C), 2016-2020, omosoft, All rights reserved
# --------------------------------------------------------
# @Name:        t9.py
# @Author:      lizhe
# @Created:     2024/10/8 - 13:26
# --------------------------------------------------------
import  random

lists = ["彭锦", "杨明海", "刘曦", "李红霞", "朱美", "高洁"]

while len(lists) > 0:
    index = random.randint(0, len(lists) - 1)
    value = lists.pop(index)
    print(value)