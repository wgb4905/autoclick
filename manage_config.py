# -*- coding: utf-8 -*-

import json
import pandas as pd
import json
import os

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
    
    generate_confidence_dict(config)


def json_to_excel(json_file, excel_file):
    """
    将 JSON 文件转换为 Excel 文件
    :param json_file: JSON 文件路径
    :param excel_file: Excel 文件路径
    """
    # 加载 JSON 文件
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 提取 files 列表
    files = data['files']
    
    # 将列表转换为 DataFrame
    df = pd.DataFrame(files)
    
    # 将 DataFrame 写入 Excel 文件
    df.to_excel(excel_file, index=False, engine='openpyxl')

    

def excel_to_json(excel_file, json_file):
    """
    根据 Excel 文件更新 JSON 配置文件
    :param excel_file: Excel 文件路径
    :param json_file: JSON 文件路径
    """
    try:
        # 读取 Excel 文件
        df = pd.read_excel(excel_file, engine='openpyxl')
        
        # 将 DataFrame 转换为字典列表
        files = df.to_dict('records')
        
        # 构建新的配置
        config = {"files": files}
        
        # 将配置写入 JSON 文件
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=4)
        
        print(f"成功更新配置文件: {json_file}")
    
    except Exception as e:
        print(f"发生错误：{e}")

    return config

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
        else:
            print("没有新增文件需要配置。")
        
    except Exception as e:
        print(f"发生错误：{e}")

    return config

def add_item(config_file, item):
    """
    在配置文件中新增一个数据项
    :param config_file: 配置文件路径
    :param item: 要新增的数据项，格式为字典
    """
    try:
        # 加载现有的配置文件
        config = load_config(config_file)
        
        # 检查是否已存在相同的 file_path
        existing_files = {file_info["file_path"] for file_info in config["files"]}
        if item["file_path"] in existing_files:
            print(f"文件路径已存在：{item['file_path']}")
            return
        
        # 新增数据项
        config["files"].append(item)
        
        # 保存配置文件
        save_config(config_file, config)
        print(f"成功新增数据项：{item}")
    
    except Exception as e:
        print(f"发生错误：{e}")

# 示例使用
if __name__ == "__main__":
    # JSON 文件路径
    json_file = 'config.json'
    
    # Excel 文件路径
    excel_file = 'config.xlsx'

    config=load_config(json_file)
    
    switch=input('请选择：\n1:json转excel\n2:excel转json\n:').strip()
    if switch== '1':
        # 调用函数，将 JSON 转换为 Excel
        json_to_excel(json_file, excel_file)
    elif switch== '2':
        # # 调用函数，根据 Excel 更新 JSON 配置文件
        config=excel_to_json(excel_file, json_file)
    else:
        print('请输入正确值')
    
    generate_confidence_dict(config)
    # 扫描文件夹，更新配置
    # folder_path='icon'
    # config=update_config(folder_path, json_file)

    