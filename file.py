import os
import cv2

# 示例使用
if __name__ == "__main__":
    # 图标文件路径
    icon_path = r"e:\autoclick\icon\dryice.png"

    # 打印文件路径
    print(f"图标路径: {icon_path}")

    # 检查文件是否存在
    if os.path.exists(icon_path):
        print("文件存在")
        # 读取图像
        image = cv2.imread(icon_path)

        if image is not None:
            print("图像读取成功")
        else:
            print("图像读取失败")
    else:
        print("文件不存在")
