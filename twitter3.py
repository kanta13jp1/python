# 必要なライブラリをインポート
import tweepy
import matplotlib.pyplot as plt

# 各種キーをセット
CONSUMER_KEY = "UdknJELvDORf0zuO6ir79em3r"
CONSUMER_SECRET = "MMFsntEXqGBxMmhAyNO7GnhdKu63uOcCMc0OmeuJrfrMp6fcfo"
ACCESS_TOKEN = "1162981636494905344-hII6sZwJFEuUHVlDV9NZEC6mPa3NMx"
ACCESS_TOKEN_SECRET = "aCQYth4FWI1Iua9iyl1doRUIP5dDCYMHRR68KR6aiY1sA"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#APIインスタンスを作成
api = tweepy.API(auth)

#自分のフォロワーのIDを取得
ids = api.get_follower_ids()

#フォロワー数とフォロー数を格納するリストを用意
follower_list = []
friend_list = []

#取得したIDそれぞれについて処理を繰り返す
for id in ids:
  #IDからユーザ情報を取得
  user_info = api.get_user(user_id=id)
  
  #ユーザ情報からフォロワー数を取得、格納
  follower = int(user_info.followers_count)
  follower_list.append(follower)

  #ユーザ情報からフォロー数を取得、格納
  friend = int(user_info.friends_count)
  friend_list.append(friend)

# フォロワー数、フォロー数のヒストグラムをそれぞれ描画
plt.hist(follower_list,bins=30)
plt.hist(friend_list,bins=30)

# フォロワー数、フォロー数の散布図を描画
plt.scatter(follower_list,friend_list)

print("終了しました")