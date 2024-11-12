# -*- coding:utf-8 -*-
# --------------------------------------------------------
# Copyright (C), 2016-2020, omosoft, All rights reserved
# --------------------------------------------------------
# @Name:        t4.py
# @Author:      lizhe
# @Created:     2024/1/4 - 21:45
# --------------------------------------------------------
import os
import time
import asyncio
import fitz
from automotive import OCRUtils, logger


async def process_page(page, abs_folder, utils):
    zoom_x = 2.0  # horizontal zoom
    zoom_y = 2.0  # vertical zoom
    mat = fitz.Matrix(zoom_x, zoom_y)
    pix = page.get_pixmap(matrix=mat)
    png_file = os.path.join(abs_folder, f"{page.number}.png")
    pix.save(png_file)
    logger.info(f"save {png_file} finished")
    contents = await utils.ocr_images(png_file)
    return contents


async def process_file(abs_file, abs_folder, utils):
    doc = fitz.open(abs_file)
    logger.info(f"handle {abs_file}")
    tasks = []

    for page in doc:
        task = process_page(page, abs_folder, utils)
        tasks.append(task)

    contents_list = await asyncio.gather(*tasks)

    with open(os.path.join(abs_folder, f"{os.path.splitext(os.path.basename(abs_file))[0]}.txt"), "w+",
              encoding="utf-8") as f:
        for contents in contents_list:
            for line in contents:
                f.write(f"{line}\n")


async def main():
    folder = r"D:\Temp\zengyu1"
    output = r"D:\Temp\output1"
    utils = OCRUtils()

    files = os.listdir(folder)
    tasks = []

    for file in files:
        abs_file = os.path.join(folder, file)
        file_name = os.path.splitext(file)[0]
        abs_folder = os.path.join(output, file_name)
        os.makedirs(abs_folder, exist_ok=True)

        task = process_file(abs_file, abs_folder, utils)
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")
