# -*- coding:utf-8 -*-
# --------------------------------------------------------
# Copyright (C), 2016-2020, lizhe, All rights reserved
# --------------------------------------------------------
# @Name:        t1.py
# @Author:      lizhe
# @Created:     2023/6/6 - 22:58
# --------------------------------------------------------
# import pathlib
# from rtfparse.parser import Rtf_Parser
# from rtfparse.renderers import de_encapsulate_html
#
# # from rtfparse import Rtf15Reader
#
# rtf_path = r'C:\Users\lizhe\Desktop\rtf\001.rtf'
# rtf_path = pathlib.Path(rtf_path)
#
# parser = Rtf_Parser(rtf_path=rtf_path)
# parsed = parser.parse_file()
#
# renderer = de_encapsulate_html.De_encapsulate_HTML()
# with open(pathlib.Path(r"C:\Users\lizhe\Desktop\test.html"), mode="w", encoding="utf-8") as html_file:
#     renderer.render(parsed, html_file)

import pathlib
from rtfparse.parser import Rtf_Parser
from rtfparse.renderers import de_encapsulate_html


source_path = pathlib.Path(r"C:\Users\lizhe\Desktop\rtf\001.rtf")
target_path = pathlib.Path(r"C:\Users\lizhe\Desktop\test.html")


parser = Rtf_Parser(rtf_path=source_path)
parsed = parser.parse_file()


renderer = de_encapsulate_html.De_encapsulate_HTML()
with open(target_path, mode="w", encoding="utf-8") as html_file:
    renderer.render(parsed, html_file)