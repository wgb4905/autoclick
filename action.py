from click_icon import click_icon, find_icon
import json

# 加载置信度
confidence_dict = {}
with open('confidence_dict.json', 'r', encoding='utf-8') as f:
    confidence_dict = json.load(f)

def get_confidence(icon_path):
    """
    获取置信度，如果配置文件中没有找到对应的置信度，使用默认置信度0.9
    :param icon_path: 图标路径
    :return: 置信度
    """
    return confidence_dict.get(icon_path, 0.9)

def find_jineng():
    icon = r'icon\button\xuan-ze-ji-neng.png'
    return find_icon(icon, get_confidence(icon))

def click_jineng(icon_paths,total=1):
    sum=0
    for icon in icon_paths:
        if click_icon(icon, get_confidence(icon)):
            sum+=1
        if sum==total:
            return True
    return False

def double_select():
    icon = r'icon\button\2-2queding.png'
    return click_icon(icon, get_confidence(icon))

def cal_jinengs():
    icon = r'icon\button\0-2queding.png'
    if find_icon(icon, get_confidence(icon)):
        return 2
    return 1

def find_jiesuan():
    icon = r'icon\button\fan-hui-ye-mian.png'
    return find_icon(icon, get_confidence(icon))

def select_jiesuan():
    icon = r'icon\button\fan-hui-ye-mian.png'
    click_icon(icon, get_confidence(icon))

def find_tiaozhan():
    icon = r'icon\button\tiaozhan.png'
    return find_icon(icon, get_confidence(icon))

def click_tiaozhan():
    icon = r'icon\button\tiaozhan.png'
    click_icon(icon, get_confidence(icon))

def find_kaishi():
    icon = r'icon\button\kai-shi-you-xi.png'
    return find_icon(icon, get_confidence(icon))

def click_kaishi():
    icon = r'icon\button\kai-shi-you-xi.png'
    return click_icon(icon, get_confidence(icon))