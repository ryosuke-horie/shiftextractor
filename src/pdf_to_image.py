# PDFファイルを画像に変換する
from pdf2image import convert_from_path # pdfを画像に変換する
import os                               # ファイルパスを扱う

# PDFファイルを画像に変換する
def convert_pdf_to_images(pdf_file_path, output_folder, output_format='jpeg'):
    # PDFファイルを画像に変換
    images = convert_from_path(pdf_file_path)

    # 画像ファイルを保存
    image_file_paths = []
    for i, image in enumerate(images):
        image_file_path = f"{output_folder}/output_{i}.{output_format}"
        image.save(image_file_path, output_format.upper())
        image_file_paths.append(image_file_path)

    return image_file_paths

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_file_path = os.path.join(current_dir, '..', 'pdf', '202304.pdf')
    output_folder = os.path.join(current_dir, '..', 'images')
    image_file_paths = convert_pdf_to_images(pdf_file_path, output_folder)

