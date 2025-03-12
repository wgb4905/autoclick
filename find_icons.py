# -*- coding: utf-8 -*-

import os
import pyautogui


    

def find_icons_from_folder(folder_path, confidence=0.9):
    """
    扫描电脑桌面，查找指定文件夹中的图标文件，并返回找到的图标文件路径列表
    :param folder_path: 包含图标文件的文件夹路径（相对路径）
    :param confidence: 图标匹配的置信度阈值（0 到 1）
    :return: 找到的图标文件路径列表
    """
    found_icons = []

    try:
        # 获取脚本所在目录
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # 构造图标的完整文件夹路径
        full_folder_path = os.path.join(script_dir, folder_path)

        # 获取文件夹中的所有 PNG 文件
        icon_files = [f for f in os.listdir(full_folder_path) if f.endswith('.png')]
        if not icon_files:
            print(f"文件夹中没有 PNG 文件：{full_folder_path}")
            return found_icons

        # 遍历图标文件
        for icon_file in icon_files:
            icon_path = os.path.join(full_folder_path, icon_file)

            # 在桌面上查找图标，使用 confidence 参数降低识别精度
            icon_location = pyautogui.locateOnScreen(icon_path, confidence=confidence)
            if icon_location:
                # 如果找到图标，将其路径添加到列表中
                found_icons.append(icon_path)
                # print(f"找到图标：{icon_path}，置信度：{confidence}")
            else:
                # print(f"未找到图标：{icon_path}，置信度：{confidence}")
                pass
    except Exception as e:
        print(f"发生错误：{e}")

    return found_icons

# 示例使用
if __name__ == "__main__":
    # 图标文件夹路径（相对路径）
    folder_path = r"icon"

    # 图标匹配的置信度阈值（0 到 1）
    confidence = 0.9  # 降低识别精度

    # 调用函数，扫描桌面并查找图标
    found_icons = find_icons_from_folder(folder_path, confidence)

    # 输出找到的图标文件路径列表
    print("找到的图标文件路径列表：")
    for icon_path in found_icons:
        print(icon_path)

    if len(found_icons)<4:
        print("有新图标没有截取到，请补充")