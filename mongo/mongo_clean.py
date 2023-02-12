import pandas as pd
from pymongo import MongoClient

if __name__ == "__main__":
    # MogoDB
    client = MongoClient("localhost", 27017)
    db = client.test
    collection = db.test

    result = collection.find({})
    df = pd.DataFrame(result)

    # _idは除外
    df = df.drop(columns='_id')

    df_clean = df.drop_duplicates()
    print(len(df_clean))
