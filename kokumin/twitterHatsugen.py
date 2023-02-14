from operator import itemgetter
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

user_list = {
    'kokumin_okayama',
    'kokumin_toyama',
    'kokumin_kyoto',
    'kokuminibaraki',
    'kokumin_myzk',
    'kokumin_tks',
    'newkokuminnara',
    'kokumin_fukuoka',
    'dpfpmiyazaki1',
    'kokumin_ymgc',
    'kokumin_fukui',
    'kokumin_chiba',
    'kokumin_kng',
    'kokumin_aichi_',
    'dpfp_fukushima',
    'KokuminHokkaido',
    'kagawakokumin',
    'kokumin_osaka',
    'dpfp_shiga',
    'dpfptokyo',
    'KokuminOita',
    'kokumin_ngsk',
    'gokokuminymgt',
    'kokumin_mie',
    'dpfp_shimane',
    'dp_tochigi',
    'n7e0jof',
    'minshin_y',
    'dpj_kagoshima',
    'minshuwakayama',
    'DPFPnews',
}

members_list = []

for screen_name in user_list:
    print(screen_name)
    user = api.get_user(screen_name=screen_name)
    # print(user)
    if (hasattr(user, 'status')):
        print(user.status.created_at)
        user_info = [user.name, '@' + user.screen_name,
                     user.statuses_count, user.status.created_at]
    else:
        user_info = [user.name, '@' + user.screen_name,
                     user.statuses_count, user.created_at]
    # print(user_info)
    # if (user.description == '' and user.statuses_count != 0):
    members_list.append(user_info)


sorted_list = sorted(members_list, key=itemgetter(3), reverse=True)
# print(*sorted_list, sep='\n')
# def follower_counts_func(acount):
#    followers_list = []
#    i = 0
#    cursor = -1
#    while cursor != 0:
#        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#        api = tweepy.API(auth, wait_on_rate_limit=True)
#        itr = tweepy.Cursor(api.get_follower_ids, id=user_list[acount], cursor=cursor).pages()
#        try:
#            for follower_id in itr.next():
#                try:
#                    # print(follower_id)
#                    user = api.get_user(screen_name="tamakiyuichiro")
#                    user_info = [user.id_str, user.screen_name, user.name, user.followers_count,user.description]
#                    print(user)
#                    followers_list.append(user_info)
#                    i = i +1
#                 #    print(i, user_info)
#                except tweepy.error.TweepError as e:
#                    print(e.reason)
#        except ConnectionError as e:
#            print(e.reason)
#        cursor = itr.next_cursor
#    return followers_list
# followers_list = follower_counts_func(acount)
# print(followers_list.size)

# フォロワーの取得
# for user_id in user_ids:
#     # print('フォロワーを取得中...', end='')
#     itr = tweepy.Cursor(api.get_follower_ids, user_id=user_id, cursor=-1).items()
#     for follower_id in itr:
#         record = pd.Series([follower_id], index=follower_ids.columns)
#         follower_ids = follower_ids.append(record, ignore_index=True)
#     print(user_id)
#     print(follower_ids.size)
#     follower_ids = pd.DataFrame([], columns=cols)

# フォローしている人の取得
# print('フォローしている人を取得中...', end='')
# itr = tweepy.Cursor(api.get_friend_ids, user_id=user_id, cursor=-1).items()
# for following_id in itr:
#     record = pd.Series([following_id], index=following_ids.columns)
#     following_ids = following_ids.append(record, ignore_index=True)
# print(' Done')

# oneside_follow = pd.DataFrame([], columns=['user_id', 'name', 'screen_name', 'description'])

# 一方的にフォローしている人を抽出
# print('一方的にフォローしている人を取得中...', end='')
# for following_id in following_ids['user_id']:
#     if following_id not in follower_ids['user_id'].values:
#         user = api.get_user(user_id=following_id)
#         record = pd.Series([user.id, user.name, user.screen_name, user.description], index=oneside_follow.columns)
#         oneside_follow = oneside_follow.append(record, ignore_index=True)
# print(' Done')

# removed_users = pd.DataFrame([], columns=['user_id', 'name', 'screen_name', 'description'])

# 一方的にフォローしている人をリムーブする
# print('以下のユーザーへのフォローを解除しました。')
# for i, user in oneside_follow.iterrows():
#     api.destroy_friendship(user_id=user.user_id)
#     removed_users = removed_users.append(user, ignore_index=True)
#     print('  アカウント名：' + user['name'] + ' / ユーザー名：' + user['screen_name'])

dir = os.path.dirname(__file__) + '/csv'
try:
    os.makedirs(dir)
except FileExistsError:
    pass
df = pd.DataFrame(sorted_list, columns=[
                  'name', 'screen_name', 'statuses_count', 'followers_count'])
df.to_csv(dir + '/Hatsugen_users_' +
          datetime.datetime.now().strftime('%y%m%d%H%M%S') + '.csv')
# removed_users.to_csv(dir + '/removed_users_' + datetime.datetime.now().strftime('%y%m%d%H%M%S') + '.csv')
