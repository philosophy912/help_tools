# -*- coding:utf-8 -*-
# --------------------------------------------------------
# Copyright (C), 2016-2020, omosoft, All rights reserved
# --------------------------------------------------------
# @Name:        t5.py
# @Author:      lizhe
# @Created:     2024/1/4 - 21:52
# --------------------------------------------------------
import argparse
import os
import time
import concurrent.futures
import fitz
from automotive import OCRUtils


def process_page(args):
    abs_file, page_number, abs_folder = args
    utils = OCRUtils()
    doc = fitz.open(abs_file)
    page = doc[page_number]

    zoom_x = 2.0
    zoom_y = 2.0
    mat = fitz.Matrix(zoom_x, zoom_y)
    pix = page.get_pixmap(matrix=mat)

    png_file = os.path.join(abs_folder, f"{page_number}.png")
    pix.save(png_file)

    contents = utils.ocr_images(png_file)
    return contents


def process_file(file_info):
    abs_file, abs_folder = file_info
    doc = fitz.open(abs_file)

    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
        args_list = [(abs_file, page.number, abs_folder) for page in doc]
        contents_list = list(executor.map(process_page, args_list))
    file_name = os.path.splitext(os.path.basename(abs_file))[0]
    file_name = file_name.replace(" ", "_")
    with open(os.path.join(output, f"{file_name}.txt"), "w+",
              encoding="utf-8") as f:
        for contents in contents_list:
            for line in contents:
                f.write(f"{line}\n")


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--folder', type=str, default=None)
    # folder = r"E:\Temp\zengyu"

    # args = parser.parse_args()
    # folder = args.folder
    folder = r"E:\Temp\files1"
    output = r"E:\Temp\output1"

    files = os.listdir(folder)
    file_info_list = []

    for file in files:
        start_time = time.time()
        abs_file = os.path.join(folder, file)
        file_name = os.path.splitext(file)[0]
        abs_folder = os.path.join(output, file_name)
        os.makedirs(abs_folder, exist_ok=True)
        # file_info_list.append((abs_file, abs_folder))
        process_file((abs_file, abs_folder))
        end_time = time.time()
        print(f"Total execution time: {end_time - start_time} seconds")
    # start_time = time.time()
    #
    # with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
    #     executor.map(process_file, file_info_list)
    #
    # end_time = time.time()
    # print(f"Total execution time: {end_time - start_time} seconds")
