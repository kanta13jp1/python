# coding:utf-8

# Pandasをインポート
import pandas as pd
import json
from pandas.io.json import json_normalize

# 変換したいJSONファイルを読み込む
df = pd.read_json('output.json')
print(df)
df.to_csv("out.csv", encoding='utf-8')

# read_jsonした結果だとネストしたjsonを展開できないのでnormalizeで展開させる
# df_json = json_normalize(df['data'])
# df_json.to_csv("out.csv", encoding='utf-8')
