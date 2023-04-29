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
                     user.statuses_count, user.status.created_at, user.followers_count]
    else:
        user_info = [user.name, '@' + user.screen_name,
                     user.statuses_count, user.created_at, user.followers_count]
    # print(user_info)
    # if (user.description == '' and user.statuses_count != 0):
    members_list.append(user_info)


sorted_list = sorted(members_list, key=itemgetter(3), reverse=True)

dir = os.path.dirname(__file__) + '/csv'
try:
    os.makedirs(dir)
except FileExistsError:
    pass
df = pd.DataFrame(sorted_list, columns=[
                  'name', 'screen_name', 'statuses_count', 'status_time', 'followers_count'])
df.to_csv(dir + '/Hatsugen_' +
          datetime.datetime.now().strftime('%y%m%d') + '.csv')
