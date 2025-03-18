import os
import json
import time
import pyautogui
import subprocess

def load_config(config_file):
    """
    加载配置文件
    :param config_file: 配置文件路径
    :return: 配置数据
    """
    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config

def save_config(config_file, config):
    """
    保存配置文件
    :param config_file: 配置文件路径
    :param config: 配置数据
    """
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=4)

def find_icon(icon_path, confidence=0.9):
    """
    查找图标
    :param icon_path: 图标文件路径
    :param confidence: 置信度
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
        return False

def open_image_with_mspaint(image_path):
    """
    使用 mspaint 打开图片
    :param image_path: 图片文件路径
    :return: mspaint 进程对象
    """
    try:
        process = subprocess.Popen(["mspaint", image_path], shell=True)
        print(f"成功使用 mspaint 打开图片：{image_path}")
        return process
    except Exception as e:
        print(f"发生错误：{e}")
        return None

def close_mspaint(process):
    """
    关闭 mspaint
    :param process: mspaint 进程对象
    """
    try:
        process.terminate()
        print("已关闭 mspaint")
    except Exception as e:
        print(f"关闭 mspaint 时发生错误：{e}")

def test_icon_recognition(config_file):
    """
    测试图标识别并更新置信度
    :param config_file: 配置文件路径
    """
    config = load_config(config_file)
    
    # 遍历配置文件中的所有文件
    for file_info in config['files']:
        icon_path = file_info['file_path']
        confidence = file_info['confidence']
        
        print(f"测试图标：{icon_path}")
        print(f"初始置信度：{confidence}")
        
        # 打开图标
        process = open_image_with_mspaint(icon_path)
        if not process:
            continue
        
        time.sleep(5)  # 等待 mspaint 完全打开
        
        # 尝试不同的置信度
        while confidence >= 0:
            if find_icon(icon_path, confidence):
                # 找到图标，更新置信度
                file_info['confidence'] = confidence
                save_config(config_file, config)
                print(f"更新置信度：{confidence}")
                break
            else:
                # 未找到图标，降低置信度
                confidence -= 0.1
                confidence = round(confidence, 1)  # 保留一位小数
        
        # 关闭 mspaint
        close_mspaint(process)
        time.sleep(2)  # 等待 mspaint 关闭

# 示例使用
if __name__ == "__main__":
    config_file = 'config.json'  # 配置文件路径
    
    # 调用测试函数
    test_icon_recognition(config_file)