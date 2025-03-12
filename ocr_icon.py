from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

def extract_text_from_icon(icon_path):
    """
    识别图标中的文字
    :param icon_path: 图标的文件路径
    :return: 图标中的文字
    """
    try:
        # 打开图标文件
        image = Image.open(icon_path)

        # 使用Tesseract进行OCR识别
        text = pytesseract.image_to_string(image)

        return text.strip()
    except Exception as e:
        return f"发生错误：{e}"

# 示例使用
if __name__ == "__main__":
    # 图标文件路径
    icon_path = r"icon\chrome_test.png"

    # 调用函数并输出识别结果
    text = extract_text_from_icon(icon_path)
    print(f"识别到的文字：{text}")
