import os
import json
import time
import pyautogui
import subprocess
from find_icons import find_icon_with_opencv
from threading import Thread
from manage_config import load_config,save_config,add_item



result={}
namedict={}
confidenceDict=load_config('confidence_dict.json')


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
        # 使用 taskkill 强制关闭 mspaint
        subprocess.run(["taskkill", "/F", "/IM", "mspaint.exe"], check=True)
        print("已关闭 mspaint")
    except subprocess.CalledProcessError as e:
        print(f"关闭 mspaint 时发生错误：{e}")

def find_confidence(icon_path,confidence):
    # 尝试不同的置信度
    while confidence >= 0:
        if find_icon_with_opencv(icon_path, threshold=confidence):
            # 找到图标，更新置信度
            print(f"最终置信度：{confidence}")
            # close_mspaint(process)
            return confidence
        else:
            # 未找到图标，降低置信度
            confidence -= 0.1
            print(f"降低置信度到:{confidence}")
            confidence = round(confidence, 1)  # 保留一位小数


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
        
        time.sleep(1)  # 等待 mspaint 完全打开
        
        # 尝试不同的置信度
        confidence=find_confidence(icon_path,confidence)

        # 找到图标，更新置信度
        file_info['confidence'] = confidence
        save_config(config_file, config)
        
        # 关闭 mspaint
        close_mspaint(process)

def thread_proces(icon_path):
    """存储每个线程返回的结果"""
    global result
    global confidenceDict
    confidence=confidenceDict.get(icon_path,0.9)
    confidence=find_confidence(icon_path,confidence)
    if confidence>0.6:
        return
    check=input('是否更新置信度：是/否 ？')
    if check == '是':
        result[icon_path]=confidence
    elif check == '否' :
        result[icon_path]=0.9
    else:
        return
            

def main():
    """
    主函数
    """
    config_file = 'config.json'  # 配置文件路径
    config = load_config(config_file)

    global namedict
    for file_info in config['files']:
        icon_path = file_info['file_path']
        name = file_info['name']
        type = file_info['type']
        namedict[(name,type)]=icon_path

    # 输入多个图片名称，用“|”隔开
    type=input("图中有几个技能(默认3)：")
    if type.strip()=='\n' or not type:
        type=3
    else:
        type=int(type)
        
    # print(f"type:{type}" )
    input_icons = input("请输入要识别的图片名称（用|隔开）：").strip().split('|')
    input_icons = [icon for icon in input_icons if icon.strip()]
    icon_paths=[]
    for icon in input_icons:
        if (icon,type) in namedict.keys():
            icon_paths.append(namedict[(icon,type)])
        else:
            inputs=input(f'未录入{icon}，是否录入？录入请输入：是/否？')
            if inputs.strip() != '是':
                continue
            item={'name':icon,"description": "默认技能描述","category": "默认","file_path": "icon\\button\\shuaxin.png","weight": 1,"confidence": 0.9}
            description=input("请输入技能描述：")
            if description :
                item["description"]=description
            category=input("请输入类别：")
            if category :
                item["category"]=category
            item["type"]=type
            file_path=input("请输入文件路径：")
            if file_path :
                file_path=os.path.join('icon',type,file_path)
                item["file_path"]=file_path
            weight=input("请输入权重 1-10：")
            if weight :
                item["weight"]=weight
            
            item["confidence"]=0.9

            add_item(config_file,item)
            config["files"].append(item)
            namedict[icon]=file_path
            icon_paths.append(file_path)

    # 创建线程列表
    print(f"开始识别图标：{icon_paths}")
    threads = []
    for icon_path in icon_paths:
        thread = Thread(target=thread_proces, args=(icon_path,))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    # for icon_path in icon_paths:
    #     thread_proces(icon_path)

    for file_info in config['files']:
        icon_path = file_info['file_path']
        confidence=file_info['confidence']
        new_confidence=result.get(icon_path,confidence)
        file_info['confidence']=new_confidence
    save_config(config_file, config)

    print("所有图标识别完成，配置文件已更新。")


# 示例使用
if __name__ == "__main__":
    config_file = 'config.json'  # 配置文件路径
    
    # 调用测试函数
    # test_icon_recognition(config_file)

    # icon_path=r"icon\wenyadanlianfa.png"
    # find_confidence(icon_path,1)
    while True:
        main()

