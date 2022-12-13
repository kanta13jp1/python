import tweepy
import pandas as pd
import os
import datetime

CONSUMER_KEY = "UdknJELvDORf0zuO6ir79em3r"
CONSUMER_SECRET = "MMFsntEXqGBxMmhAyNO7GnhdKu63uOcCMc0OmeuJrfrMp6fcfo"
ACCESS_TOKEN = "1162981636494905344-hII6sZwJFEuUHVlDV9NZEC6mPa3NMx"
ACCESS_TOKEN_SECRET = "aCQYth4FWI1Iua9iyl1doRUIP5dDCYMHRR68KR6aiY1sA"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
screen_name = 'kanta13jp1'  # <- あなたのユーザーID

cols = ['user_id']
follower_ids = pd.DataFrame([], columns=cols)
following_ids = pd.DataFrame([], columns=cols)

# フォロワーの取得
print('フォロワーを取得中...', end='')
itr = tweepy.Cursor(api.get_follower_ids, screen_name=screen_name, cursor=-1).items()
for follower_id in itr:
    record = pd.Series([follower_id], index=follower_ids.columns)
    follower_ids = follower_ids.append(record, ignore_index=True)
print(' Done')

# フォローしている人の取得
print('フォローしている人を取得中...', end='')
itr = tweepy.Cursor(api.get_friend_ids, screen_name=screen_name, cursor=-1).items() 
for following_id in itr:
    record = pd.Series([following_id], index=following_ids.columns)
    following_ids = following_ids.append(record, ignore_index=True)
print(' Done')

oneside_follow = pd.DataFrame([], columns=['user_id', 'name', 'screen_name', 'description'])

# 一方的にフォローしている人を抽出
print('一方的にフォローしている人を取得中...', end='')
for following_id in following_ids['user_id']:
    if following_id not in follower_ids['user_id'].values:
        user = api.get_user(user_id=following_id)
        print(user.screen_name)
        record = pd.Series([user.id, user.name, user.screen_name, user.description], index=oneside_follow.columns)
        oneside_follow = oneside_follow.append(record, ignore_index=True)
print(' Done')

removed_users = pd.DataFrame([], columns=['user_id', 'name', 'screen_name', 'description'])

# 一方的にフォローしている人をリムーブする
print('以下のユーザーへのフォローを解除しました。')
for i, user in oneside_follow.iterrows():
    api.destroy_friendship(user_id=user.user_id)
    removed_users = removed_users.append(user, ignore_index=True)
    print('  アカウント名：' + user['name'] + ' / ユーザー名：' + user['screen_name'])

dir = os.path.dirname(__file__) + '/csv'
try:
    os.makedirs(dir)
except FileExistsError:
    pass
removed_users.to_csv(dir + '/removed_users_' + datetime.datetime.now().strftime('%y%m%d%H%M%S') + '.csv')