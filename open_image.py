import os
import subprocess
import pyautogui
import time

def open_image_with_default_app(image_path):
    """
    使用 Windows 系统自带的默认图片查看器打开图片
    :param image_path: 图片文件的路径
    """
    try:
        # 使用 os.startfile 打开图片
        os.startfile(image_path)
        print(f"成功打开图片：{image_path}")
    except Exception as e:
        print(f"发生错误：{e}")

def open_image_with_photos_app(image_path):
    """
    使用 Windows 自带的“照片”应用程序打开图片
    :param image_path: 图片文件的路径
    """
    try:
        # 使用 subprocess 调用“照片”应用程序
        subprocess.run(["mspaint", image_path], shell=True)
        print(f"成功使用“照片”应用程序打开图片：{image_path}")
    except Exception as e:
        print(f"发生错误：{e}")

def switch_image_in_mspaint(new_image_path):
    """
    在 mspaint 中切换打开的图片文件路径
    :param new_image_path: 新图片文件的路径
    """
    try:
        pyautogui.getActiveWindow().activate()  # 激活 mspaint 窗口

        # 模拟键盘快捷键 Ctrl + O 打开“打开文件”对话框
        pyautogui.hotkey('ctrl', 'o')
        time.sleep(1)  # 等待对话框打开

        # 输入新图片文件的路径
        pyautogui.write(new_image_path)
        time.sleep(1)  # 等待路径输入完成

        # 模拟按下 Enter 键确认打开
        pyautogui.press('enter')
        print(f"成功在 mspaint 中切换图片：{new_image_path}")
    except Exception as e:
        print(f"发生错误：{e}")

# 示例使用
if __name__ == "__main__":
    image_path = r'E:\autoclick\icon'  # 替换为你的图片路径

    # 使用默认图片查看器打开图片
    # open_image_with_default_app(image_path)

    # 使用“照片”应用程序打开图片
    # open_image_with_photos_app(image_path

    # open_image_with_photos_app(r'E:\autoclick\icon\bao-zha-hua-huo.png')
    subprocess.Popen(["mspaint"], shell=True)

    time.sleep(5)

    image_paths=[os.path.join(image_path,f) for f in os.listdir(image_path) if f.endswith('.png')]

    max=5
    i=0
    for p in image_paths:
        print(p)
        switch_image_in_mspaint(p)
        i+=1
        if i > max:
            break
