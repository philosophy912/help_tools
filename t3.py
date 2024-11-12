# -*- coding:utf-8 -*-
# --------------------------------------------------------
# Copyright (C), 2016-2020, omosoft, All rights reserved
# --------------------------------------------------------
# @Name:        t3.py
# @Author:      lizhe
# @Created:     2023/12/7 - 21:09
# --------------------------------------------------------
import argparse
import os
import time

import fitz
from automotive import OCRUtils, logger

folder = r"D:\Workspace\github\help_tools\zengyu"


def parse(folder_args: str):
    utils = OCRUtils()
    output = r"D:\Workspace\github\help_tools\output"
    files = os.listdir(folder_args)

    for file in files:
        abs_file = os.path.join(folder_args, file)
        file_name = os.path.splitext(file)[0]
        abs_folder = os.path.join(output, file_name)
        os.makedirs(abs_folder, exist_ok=True)
        doc = fitz.open(abs_file)
        abs_txt = os.path.join(abs_folder, f"{file_name}.txt")
        with open(abs_txt, "w+", encoding="utf-8") as f:
            index = 1
            for page in doc:
                logger.info(f"parse {index} page")
                zoom_x = 2.0  # horizontal zoom
                zoom_y = 2.0  # vertical zoom
                mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension
                pix = page.get_pixmap(matrix=mat)  # render page to an image
                # 转换pixmap为np.ndarray
                # print(type(pix))
                png_file = os.path.join(abs_folder, f"{page.number}.png")
                start = time.time()
                pix.save(png_file)
                # end = time.time()
                # print(f"pass time is {end - start}")
                # start = time.time()
                contents = utils.ocr_images(png_file)
                logger.info(f"第{index}页解析结果是{contents}")
                # end = time.time()
                # print(f"pass time is {end - start}")
                for line in contents:
                    f.writelines(f"{line}\n")
                index += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', type=str, default=None)
    args = parser.parse_args()
    folder = args.folder
    print(folder)
    parse(folder)
