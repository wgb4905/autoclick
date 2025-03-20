# -*- coding: utf-8 -*-

import json
import os
from manage_config import load_config

def calculate_file_weights(config, category_weights):
    """
    计算每个文件的最终权重
    :param config: 配置文件内容
    :param category_weights: 类别的权重字典
    :return: 文件名和最终权重的字典
    """
    file_weights_3 = {}
    file_weights_4 = {}

    # 遍历配置文件中的文件
    for file_info in config['files']:
        file_path = file_info['file_path']
        category = file_info['category']
        file_weight = file_info['weight']
        type=file_info['type']

        # 计算最终权重
        final_weight = category_weights.get(category,1) * file_weight
        
        if int(type )==3:
            file_weights_3[file_path] = final_weight
        elif int(type )==4:
            file_weights_4[file_path] = final_weight

    return file_weights_3,file_weights_4

def get_sorted_weights(file_weights):
    """
    按最终权重由大到小排序
    :param file_weights: 文件名和最终权重的字典
    :return: 按最终权重由大到小排序的列表
    """
    # 按权重排序，返回一个包含 (文件名, 权重) 的列表
    sorted_weights = sorted(file_weights.items(), key=lambda x: int(x[1]), reverse=True)
    files = [i[0] for i in sorted_weights if int(i[1]) > 0]
    return files



def persist_weight_results(category_weights_str, sorted_files,t):
    """
    将类别权重字典转换为字符串，并持久化结果
    :param category_weights_str: 类别权重字典的字符串表示
    :param sorted_files: 按权重排序的文件列表
    :return: None
    """
    weight_results = {category_weights_str: sorted_files}
    if int(t)==3:
        with open('weight_results_3.json', 'w', encoding='utf-8') as f:
            json.dump(weight_results, f, ensure_ascii=False, indent=4)
    elif int(t)==4:
        with open('weight_results_4.json', 'w', encoding='utf-8') as f:
            json.dump(weight_results, f, ensure_ascii=False, indent=4)

def load_weight_results(t):
    """
    加载持久化的权重结果
    :return: 权重结果字典
    """
    if int(t)==3:
        if os.path.exists('weight_results_3.json'):
            with open('weight_results_3.json', 'r', encoding='utf-8') as f:
                return json.load(f)
    elif int(t)==4:
        if os.path.exists('weight_results_4.json'):
            with open('weight_results_4.json', 'r', encoding='utf-8') as f:
                return json.load(f)
    return {}

def query_sorted_files(category_weights,t):
    """
    查询功能：根据类别权重字典返回排序后的文件列表
    :param category_weights: 类别的权重字典
    :return: 按权重排序的文件列表
    """
    category_weights_str = json.dumps(category_weights, sort_keys=True)
    weight_results = load_weight_results(t)

    if category_weights_str in weight_results.keys():
        return weight_results[category_weights_str]
    else:
        config = load_config('config.json')
        file_weights_3,file_weights_4 = calculate_file_weights(config, category_weights)
        sorted_files_3 = get_sorted_weights(file_weights_3)
        persist_weight_results(category_weights_str, sorted_files_3,3)
        sorted_files_4 = get_sorted_weights(file_weights_4)
        persist_weight_results(category_weights_str, sorted_files_4,4)
        if int(t)==3:
            return sorted_files_3
        elif int(t)==4:
            return sorted_files_4

# 示例使用
if __name__ == "__main__":
    # 配置文件路径
    config_file = 'config.json'

    # 类别的权重字典
    category_weights = {
        "A": 2,
        "B": 1.5,
        "C": 1
    }

    # 加载配置文件
    config = load_config(config_file)


    # 查询功能
    sorted_files = query_sorted_files(category_weights,3)

    # 输出结果
    print("按权重排序的文件列表：")
    print(sorted_files)