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
    'CDP2017',
    'DPFPnews',
}

members_list = []

rikken_follower = 0
rikken_sabun = 0
kokumin_follower = 0
kokumin_sabun = 0
sabun = 0

for screen_name in user_list:
    print(screen_name)
    user = api.get_user(screen_name=screen_name)

    if user.name == '立憲民主党':
        rikken_follower: int = user.followers_count
        user_info = [user.name, '@' + user.screen_name,
                     rikken_follower, rikken_follower - 191458]
    else:
        kokumin_follower: int = user.followers_count
        user_info = [user.name, '@' + user.screen_name,
                     kokumin_follower, kokumin_follower - 56367]
    print(user_info)
    members_list.append(user_info)

print(f'{rikken_follower} and {kokumin_follower}')

sabun = (rikken_follower - kokumin_follower)
print(sabun)
user_info = ['差分', '', sabun, sabun - 135091]


sorted_list = sorted(members_list, key=itemgetter(2), reverse=True)
sorted_list.append(user_info)

print(*sorted_list, sep='\n')

dir = os.path.dirname(__file__) + '/csv'
try:
    os.makedirs(dir)
except FileExistsError:
    pass
df = pd.DataFrame(sorted_list, columns=[
                  'name', 'screen_name', 'followers_count', 'sabun'])
df.to_csv(dir + '/Hikaku_' +
          datetime.datetime.now().strftime('%y%m%d') + '.csv')
# removed_users.to_csv(dir + '/removed_users_' + datetime.datetime.now().strftime('%y%m%d%H%M%S') + '.csv')
