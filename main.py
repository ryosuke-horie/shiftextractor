import os
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
from src.detect_text import detect_text
from src.extract_shift_data import extract_shift_data
from src.pdf_to_image import convert_pdf_to_images

def main():
    name = '田'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_file_path = os.path.join(current_dir, 'pdf', '202304.pdf')
    output_folder = os.path.join(current_dir, 'images')

    # PDFファイルを画像に変換
    image_file_paths = convert_pdf_to_images(pdf_file_path, output_folder)

    for image_file_path in image_file_paths:
        # 画像ファイルからテキストデータを抽出
        text = detect_text(image_file_path)
        print(f'Text extracted from {image_file_path}:\n{text}\n')

        # テキストデータから指定された名前に関連するシフトデータを抽出
        shift_data = extract_shift_data(text, name)
        print(f'Shift data for {name} in {image_file_path}: {shift_data}')

if __name__ == '__main__':
    main()
