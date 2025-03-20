import calculate_weights
import os
import action
import click_icon
import time
import json

#技能大类优先级
category_weights = {
    "干冰弹": 10,
    "枪": 10,
    "温压弹": 5,
    "车":5
}


#0.查找图标文件（按优先级排列）
icons_3 = calculate_weights.query_sorted_files(category_weights,3)
icons_4 = calculate_weights.query_sorted_files(category_weights,4)
#加载置信度
confidence_dict={}
with open('confidence_dict.json', 'r', encoding='utf-8') as f:
    confidence_dict = json.load(f)



#1.选择技能
def main():
    """
    主函数，每隔 5 秒扫描一次桌面，执行对应操作
    """
    print("开始扫描")
    while True:
        #判断是哪个页面
        if action.find_jineng():
            #技能选择页面
            print("开始选择技能")
            total=action.cal_jinengs()
            print(f"需要选择{total}个技能")
            if total==2:
                icons=icons_4
            else:
                icons=icons_3
            if action.click_jineng(icons,total):
                if total ==2 :
                    if not action.double_select():
                        print("没有找到双选提交按钮")
                        break    
        elif action.find_jiesuan():
            #结算页面  
            action.select_jiesuan()
            print("点击返回")
        elif action.find_tiaozhan():
            #挑战页面
            action.click_tiaozhan()
            print("点击挑战")
        elif action.find_kaishi():
            action.click_kaishi()
            print("点击开始")
        else:
            print("pass")
            time.sleep(1)
        
        #调试
        # break
        # 等待 5 秒钟
        


if __name__ == "__main__":
    main()
    # pass