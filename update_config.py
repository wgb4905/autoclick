# -*- coding: utf-8 -*-

import os
import json


def generate_confidence_dict(config):
    """
    生成 {file_path: confidence} 字典并持久化
    :param config: 配置文件内容
    :return: None
    """
    confidence_dict = {file_info['file_path']: file_info['confidence'] for file_info in config['files']}
    with open('confidence_dict.json', 'w', encoding='utf-8') as f:
        json.dump(confidence_dict, f, ensure_ascii=False, indent=4)

def update_config(folder_path, config_file):
    """
    根据指定文件夹中的文件更新 config.json 文件，只新增未配置的文件
    :param folder_path: 包含图标文件的文件夹路径
    :param config_file: 配置文件路径
    """
    try:
        # 获取文件夹中的所有 PNG 文件
        icon_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.png')]
        if not icon_files:
            print(f"文件夹中没有 PNG 文件：{folder_path}")
            return

        # 加载现有的配置文件
        if os.path.exists(config_file):
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
        else:
            config = {"files": []}

        # 获取已配置的文件名列表
        existing_files = {file_info["file_path"] for file_info in config["files"]}

        # 新增未配置的文件
        new_files = [
            {
                "name": "技能名称",
                "file_path": icon_file,
                "category": "默认",
                "weight": 1,
                "confidence": 0.9,  # 默认置信度
                "description": "默认技能描述"  # 默认技能描述
            }
            for icon_file in icon_files
            if icon_file not in existing_files
        ]

        if new_files:
            config["files"].extend(new_files)
            # 将配置文件内容写入 config.json
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=4)
            print(f"新增文件配置：{new_files}")

            # 更新 confidence_dict.json
            generate_confidence_dict(config)
        else:
            print("没有新增文件需要配置。")
        
    except Exception as e:
        print(f"发生错误：{e}")

# 示例使用
if __name__ == "__main__":
    # 图标文件夹路径
    folder_path = r"icon"

    # 配置文件路径
    config_file = r"config.json"

    # 调用函数，更新配置文件
    update_config(folder_path, config_file)