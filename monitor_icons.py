# -*- coding: utf-8 -*-

import time
import subprocess
import find_icons

# 图标文件夹路径（相对路径）
folder_path = r"icon"

# 图标匹配的置信度阈值（0 到 1）
confidence = 0.9  # 降低识别精度

def main():
    """
    主函数，每隔 5 秒钟执行一次 find_icon.py，直到找到的图标列表长度小于 4
    """
    while True:
        # 执行 find_icon.py 脚本
        found_icons = find_icons.find_icons_from_folder(folder_path, confidence)
        
        # 如果找到的图标列表长度为0，则继续执行
        if len(found_icons) == 0:
            print("找到的图标列表长度为0，继续监控。")
            continue

        # 输出找到的图标文件路径列表
        print("找到的图标文件路径列表：")
        for icon_path in found_icons:
            print(icon_path)

        
        # 如果找到的图标列表长度小于 4，则停止
        if len(found_icons) < 4:
            print("找到的图标列表长度小于 4，停止执行。")
            # break

        if len(found_icons) == 4:
            # 等待 5 秒钟
            time.sleep(1)
        
        

# 示例使用
if __name__ == "__main__":
    main()
