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
    # df = df.drop(columns='_id')
    print(df)
    for i in range(len(df)):
        # print(df.iat[i, 1].splitlines())
        data = df.iat[i, 2].splitlines()
        # print(len(data))
        if (len(data) == 4):
            print("No." + str(i + 1))
            print(data[0])
            print(data[1])
            print(data[2])
            print(data[3])
            print('\n')
            # print("OK")
        elif (len(data) == 5):
            print(data[0])
            print(data[1])
            print(data[2])
            print(data[3])
            print(data[4])
            print(df.iat[i, 1])
            concat = data[0] + data[1] + '\n' + \
                data[2] + '\n' + data[3] + '\n' + data[4]
            print(concat)
            update = collection.update_one(
                {'No': df.iat[i, 1]}, {'$set': {'data': concat}})
            print('更新件数：' + str(update.matched_count))
            # print("\n")

    print(df.duplicated().value_counts())
