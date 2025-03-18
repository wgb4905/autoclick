# -*- coding: utf-8 -*-

import os
import pyautogui
import time

def find_icon(icon_path, confidence=0.9):
    """
    扫描电脑桌面，查找指定文件夹中的图标文件，并返回找到的图标文件路径列表
    :param icon_path: 图标文件的文件夹路径（相对路径）
    :param confidence: 图标匹配的置信度阈值（0 到 1）
    :return: 是否找到图标
    """
    try:
        icon_location = pyautogui.locateOnScreen(icon_path, confidence=confidence)
        if icon_location:
            print(f"找到图标：{icon_path}，置信度：{confidence}")
            return True
        else:
            print(f"未找到图标：{icon_path}，置信度：{confidence}")
            return False
    except Exception as e:
        print(f"发生错误：{e}")

def click_icon(icon_path, delay=0, confidence=0.9):
    """
    识别图标并点击
    :param icon_path: 图标的文件路径
    :param delay: 鼠标移动到图标位置后到点击的间隔时间（秒）
    :param confidence: 图标匹配的置信度阈值（0 到 1）
    """
    try:
        print(f"开始点击{icon_path}")
        icon_location = pyautogui.locateOnScreen(icon_path, confidence=confidence)
        if icon_location:
            icon_center = pyautogui.center(icon_location)
            pyautogui.moveTo(icon_center.x, icon_center.y)
            time.sleep(delay)
            pyautogui.click()
            print(f"成功点击图标：{icon_path}")
            return True
        else:
            print(f"未找到图标：{icon_path}")
            return False
    except Exception as e:
        print(f"发生错误：{e}")

# 示例使用
if __name__ == "__main__":
    # 图标文件路径（相对于脚本目录）
    icon_path = r'icon\jiao-tu-zheng-ce.png'

    # 鼠标移动到图标位置后到点击的间隔时间（秒）
    delay = 0

    # 动态调整置信度
    confidence = 0.7  # 初始置信度

    #显示器的分辨率
    print(pyautogui.size())

    # 尝试不同的置信度
    for conf in [0.7, 0.8, 0.9]:
        if find_icon(icon_path, conf):
            click_icon(icon_path, delay, conf)
            break
