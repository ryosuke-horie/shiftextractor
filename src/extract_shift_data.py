import re

def extract_shift_data(text, name):
    # 日付とシフトデータを抽出する正規表現パターンを定義
    date_pattern = r'(\d{1,2})'
    shift_pattern = r'(\d{3,4}-\d{3,4})'

    # 名前を探すための正規表現パターンを定義
    name_pattern = re.compile(fr'{name}\s*{shift_pattern}')

    # シフトデータを格納するためのリストを初期化
    shift_data = []

    # テキストデータから名前に関連するシフトデータを検索
    for match in name_pattern.finditer(text):
        shift = match.group(1)
        date_index = match.start() - 1

        # 日付を検索
        date_match = re.search(date_pattern, text[:date_index][::-1])
        if date_match:
            date = int(date_match.group(1)[::-1])

            # 日付とシフトデータをタプルとしてリストに追加
            shift_data.append((date, shift))

    return shift_data
