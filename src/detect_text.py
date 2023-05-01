from google.cloud import vision_v1
from google.cloud.vision_v1 import types
import io

def detect_text(image_path):
    client = vision_v1.ImageAnnotatorClient()

    # 画像を読み込む
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # 特徴量設定を作成
    feature = types.Feature(
        type_=vision_v1.Feature.Type.TEXT_DETECTION,
    )

    # ImageAnnotatorClientに渡すリクエストを作成
    request = types.AnnotateImageRequest(
        image=image,
        features=[feature],
        image_context=types.ImageContext(language_hints=["ja"])
    )

    response = client.annotate_image(request=request)

    # 検出されたテキストを返す
    text = response.full_text_annotation.text
    return text

if __name__ == "__main__":
    # 仮の画像ファイルパス
    image_file_path = "path/to/your/image/file.jpg"

    text = detect_text(image_file_path)
    print(f"Text extracted from {image_file_path}:\n{text}\n")
