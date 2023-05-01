from src.pdf_to_image import convert_pdf_to_images
from src.detect_text import detect_text
import os

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_file_path = os.path.join(current_dir, 'pdf', '202304.pdf')
    output_folder = os.path.join(current_dir, 'images')
    
    image_file_paths = convert_pdf_to_images(pdf_file_path, output_folder)

    for image_file_path in image_file_paths:
        text = detect_text(image_file_path)
        print(f"Text extracted from {image_file_path}:\n{text}\n")

if __name__ == "__main__":
    main()
