# -*- coding: utf-8 -*-

import json
import pandas as pd

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

# 示例使用
if __name__ == "__main__":
    # JSON 文件路径
    json_file = 'config.json'
    
    # Excel 文件路径
    excel_file = 'config.xlsx'
    
    # 调用函数，将 JSON 转换为 Excel
    # json_to_excel(json_file, excel_file)
    
    # 调用函数，根据 Excel 更新 JSON 配置文件
    excel_to_json(excel_file, json_file)