import json
import csv
# import pandas as pd

# CSVファイルの読み込み
with open('json_csv/target.csv', 'r', encoding="utf-8") as f:
    dreader = csv.DictReader(f)
    d_list = [row for row in dreader]
    print(d_list)

# df = pd.read_csv("test.csv")
# df["size"] = df["sizeW"].astype(str) + ' × ' + df["sizeH"].astype(str)
# df2 = df.loc[:, ["id", "name", "size"]]
# print(df2)

# 文字列として出力
json_text = json.dumps(d_list, indent=2, ensure_ascii=False)
print(json_text)

# JSONファイルへの書き込み
with open('json_csv/output.json', 'w', encoding='utf-8') as f:
    json.dump(d_list, f, indent=2, ensure_ascii=False)
