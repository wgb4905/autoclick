# -*- coding: utf-8 -*-

import json
from click_icon import find_icon

# 加载配置文件
def load_config(config_file):
    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config

# 根据技能名称查找图标路径和置信度
def find_icon_info_by_name(config, skill_name):
    for file_info in config['files']:
        if file_info['name'] == skill_name:
            return file_info['file_path'], file_info['confidence']
    return None, None

# 测试图标识别
def test_icon_recognition(config_file, skill_name):
    # 加载配置文件
    config = load_config(config_file)
    
    # 查找图标路径和置信度
    icon_path, confidence = find_icon_info_by_name(config, skill_name)
    
    if icon_path is None:
        print(f"未找到技能名称: {skill_name}")
        return
    
    print(f"技能名称: {skill_name}")
    print(f"图标路径: {icon_path}")
    print(f"置信度: {confidence}")
    
    # 调用 find_icon 方法进行识别
    while True:
        result = find_icon(icon_path, confidence)
        if result:
            print(f"成功识别图标: {icon_path}，置信度: {confidence}")
            break
        else:
            print(f"未识别到图标: {icon_path}，置信度: {confidence}")
            # 调整置信度
            new_confidence = float(input("请输入新的置信度（0 到 1 之间）："))
            if 0 <= new_confidence <= 1:
                confidence = new_confidence
            else:
                print("置信度必须在 0 到 1 之间，请重新输入。")

# 示例使用
if __name__ == "__main__":
    # 配置文件路径
    config_file = 'config.json'

    while True:
    
        # 输入要测试的技能名称
        skill_name = input("请输入要测试的技能名称：")
        
        # 调用测试函数
        test_icon_recognition(config_file, skill_name)
