# -*- coding: utf-8 -*-

import os
import pyautogui
import time
import cv2
import numpy as np


def find_icon_with_opencv(icon_path, screenshot=None, threshold=0.8):
    """
    使用 OpenCV 进行模板匹配查找图标
    :param icon_path: 图标文件路径
    :param screenshot: 屏幕截图（可选）
    :param threshold: 匹配阈值
    :return: 是否找到图标
    """
    if screenshot is None:
        screenshot = pyautogui.screenshot()
        # print("屏幕尺寸是：",pyautogui.size())
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    icon = cv2.imread(icon_path, cv2.IMREAD_UNCHANGED)
    result = cv2.matchTemplate(screenshot, icon, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        # 计算图标中心坐标
        icon_height, icon_width = icon.shape[:2]
        center_x = max_loc[0] + icon_width // 2
        center_y = max_loc[1] + icon_height // 2
        print(f"找到图标：{icon_path}，匹配度：{max_val}，中心坐标：({center_x}, {center_y})")
        pyautogui.moveTo(center_x, center_y)
        return (center_x, center_y)
    else:
        print(f"未找到图标：{icon_path}，匹配度：{max_val}")
        return None

def find_icon(icon_path, confidence=0.9):
    """
    扫描电脑桌面，查找指定文件夹中的图标文件，并返回找到的图标文件路径列表
    :param icon_path: 图标文件的文件夹路径（相对路径）
    :param confidence: 图标匹配的置信度阈值（0 到 1）
    :return: 是否找到图标
    """

    try:
        # print(f"寻找图标：{icon_path}")
        # 在桌面上查找图标，使用 confidence 参数降低识别精度
        # icon_location = pyautogui.locateOnScreen(icon_path, confidence=confidence)
        #使用opencv方法
        icon_location = find_icon_with_opencv(icon_path, threshold=confidence)
        if icon_location:
            # 如果找到图标，将其路径添加到列表中
            print(f"找到图标：{icon_path}，置信度：{confidence}")
            return True
        else:
            # print(f"未找到图标：{icon_path}，置信度：{confidence}")
            return False
    except Exception as e:
        print(f"发生错误：{e}")

def click_icon(icon_path,  confidence=0.9,delay=0):
    """
    识别图标并点击
    :param icon_path: 图标的文件路径
    :param delay: 鼠标移动到图标位置后到点击的间隔时间（秒）
    :param confidence: 图标匹配的置信度阈值（0 到 1）
    """
    try:
        # 在屏幕上查找图标，使用 confidence 参数降低识别精度
        print(f"开始点击{icon_path}")
        icon_location = find_icon_with_opencv(icon_path, threshold=confidence)
        if icon_location:
            # 获取图标的中心位置
            # icon_center = pyautogui.center(icon_location)

            # 移动鼠标到图标中心位置
            # pyautogui.moveTo(icon_location[0], icon_location[0])

            # 等待指定的时间
            time.sleep(delay)

            # 点击图标
            pyautogui.click()
            print(f"成功点击图标：{icon_path}")
            return True
        else:
            # print(f"未找到图标：{icon_path}")
            return False
            pass
    except Exception as e:
        print(f"发生错误：{e}")

# 示例使用
if __name__ == "__main__":
    # 获取脚本所在目录
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # 图标文件路径（相对于脚本目录）
    icon_path = 'icon\\1\\2-2queding.png'

    # 鼠标移动到图标位置后到点击的间隔时间（秒）
    delay = 0

    # 图标匹配的置信度阈值（0 到 1）
    confidence = 0.8  # 降低识别精度

    # find_icon(icon_path,confidence)

    # 调用函数
    click_icon(icon_path, confidence, delay)