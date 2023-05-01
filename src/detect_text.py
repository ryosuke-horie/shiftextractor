from google.cloud import vision
import io

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    return texts[0].description if texts else ""

if __name__ == "__main__":
    # 仮の画像ファイルパス
    image_file_path = "path/to/your/image/file.jpg"

    text = detect_text(image_file_path)
    print(f"Text extracted from {image_file_path}:\n{text}\n")

