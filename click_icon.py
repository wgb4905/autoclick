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
        # print(f"寻找图标：{icon_path}")
        # 在桌面上查找图标，使用 confidence 参数降低识别精度
        icon_location = pyautogui.locateOnScreen(icon_path, confidence=confidence)
        if icon_location:
            # 如果找到图标，将其路径添加到列表中
            print(f"找到图标：{icon_path}，置信度：{confidence}")
            return True
        else:
            # print(f"未找到图标：{icon_path}，置信度：{confidence}")
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
        # 在屏幕上查找图标，使用 confidence 参数降低识别精度
        print(f"开始点击{icon_path}")
        icon_location = pyautogui.locateOnScreen(icon_path, confidence=confidence)
        if icon_location:
            # 获取图标的中心位置
            icon_center = pyautogui.center(icon_location)

            # 移动鼠标到图标中心位置
            pyautogui.moveTo(icon_center.x, icon_center.y)

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
    icon_path = r'icon\jiao-tu-zheng-ce.png'

    # 鼠标移动到图标位置后到点击的间隔时间（秒）
    delay = 0

    # 图标匹配的置信度阈值（0 到 1）
    confidence = 0.7  # 降低识别精度

    find_icon(icon_path,0.7)

    # 调用函数
    click_icon(icon_path, delay, confidence)