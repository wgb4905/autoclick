# -*- coding: utf-8 -*-

import action

def test_find_jineng():
    """
    测试 find_jineng 函数
    """
    result = action.find_jineng()
    print(f"测试 find_jineng: {'成功' if result else '失败'}")

def test_click_jineng():
    """
    测试 click_jineng 函数
    """
    icon_paths = [r'icon\button\xuan-ze-ji-neng.png']
    result = action.click_jineng(icon_paths)
    print(f"测试 click_jineng: {'成功' if result else '失败'}")

def test_double_select():
    """
    测试 double_select 函数
    """
    result = action.double_select()
    print(f"测试 double_select: {'成功' if result else '失败'}")

def test_cal_jinengs():
    """
    测试 cal_jinengs 函数
    """
    result = action.cal_jinengs()
    print(f"测试 cal_jinengs: 返回值为 {result}")

def test_find_jiesuan():
    """
    测试 find_jiesuan 函数
    """
    result = action.find_jiesuan()
    print(f"测试 find_jiesuan: {'成功' if result else '失败'}")

def test_select_jiesuan():
    """
    测试 select_jiesuan 函数
    """
    action.select_jiesuan()
    print("测试 select_jiesuan: 执行完毕")

def test_find_tiaozhan():
    """
    测试 find_tiaozhan 函数
    """
    result = action.find_tiaozhan()
    print(f"测试 find_tiaozhan: {'成功' if result else '失败'}")

def test_click_tiaozhan():
    """
    测试 click_tiaozhan 函数
    """
    action.click_tiaozhan()
    print("测试 click_tiaozhan: 执行完毕")

def test_find_kaishi():
    """
    测试 find_kaishi 函数
    """
    result = action.find_kaishi()
    print(f"测试 find_kaishi: {'成功' if result else '失败'}")

def test_click_kaishi():
    """
    测试 click_kaishi 函数
    """
    result = action.click_kaishi()
    print(f"测试 click_kaishi: {'成功' if result else '失败'}")

# 示例使用
if __name__ == "__main__":
    # 测试所有函数
    # test_find_jineng()
    # test_click_jineng()
    # test_double_select()
    # test_cal_jinengs()
    # test_find_jiesuan()
    # test_select_jiesuan()
    # test_find_tiaozhan()
    # test_click_tiaozhan()
    # test_find_kaishi()
    # test_click_kaishi()
    pass
