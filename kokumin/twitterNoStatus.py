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
    'hashimoto_lo',
    'hyakukei',
    'akiyoshi1625',
    'msakamoto1971',
    'doikousuke',
    'kou_mizuochi',
    'ishiharaseiji21',
    'Shunichirou_S',
    'KandaMihokms',
    'taueta77',
    'Naxako75',
    'kokumin_okayama',
    'Oharakazuki309',
    'ttkawa7',
    'reikotokuyama',
    'ATSUYA_SEIJI',
    'Yukiko_Kudo281',
    '25_ishida',
    'kusakawajimusho',
    'TakuyaYoshio',
    'sakai_tsuneo__',
    'kitaue_akihito7',
    'sakagamishoei',
    'kyota0498',
    'naganohirohisa',
    'nadeshiko1000',
    'boasorte0411',
    'jun_shichinohe',
    'gomi1980',
    'nakanoYo_1',
    'obatanorihito',
    'tadayuki802',
    'itoanna107',
    'ryomaeda_saw',
    'AmanoMasaki',
    'shota_inotsume',
    'JunMaru22592427',
    'Takanori_Chonan',
    'n7e0jof',
    'kokumin_toyama',
    'kokumin_kyoto',
    'isato_konagi',
    'uechannel249',
    '1orlxjTuNSHD5Ww',
    'bdxSvtQ8nQ1f7BE',
    'NaokiOgura_noda',
    '3inE5enMJrYHSf5',
    'yuuko_i10',
    'mukoyama_kobe',
    'ishiwata_yukio',
    'hide_ytr',
    'z7BJTtv5ZyaZP0i',
    'LbtKqwBMbZFMnyy',
    'HirooKataya',
    'futaikumiyo',
    'yamanefumikogm1',
    '0312_toru',
    'matsudamineyuki',
    'urakawamasami',
    'hidakasho8',
    'abe_rikiya',
    'nh19911991',
    'fujii_toshiyuki',
    'kenitani',
    'katano_36',
    'DPFP_DietInfo',
    'yoshinomasato',
    'Kobayashi1623',
    'sizuoka35bank',
    'masatomoriya',
    'takunari_ishida',
    'harada_tsm22',
    'mikisanuki2023',
    'hanako_onuki',
    'osawanoboru',
    'SekiguchiTaichi',
    'okatakashi_oota',
    'ikenaga1987',
    'shiraiwa_net',
    'maru_ko_enkai',
    'sudakazuyuki',
    'marboyanbo',
    'shuheikishimoto',
    'shinya8484',
    'YurikoOtani',
    'kenbo_yamagata',
    'satoyasuki7',
    'mihojimukyoku',
    'chimbeyoshihiro',
    'juntarotakeuchi',
    'YamazakiMaya',
    'Uematsu1987',
    'kaori_kokumin',
    'akimitsukurogi',
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
    'FeFQFsgref5wS6U',
    'kadayukiko',
    'hagamichiya',
    'kennichisakurai',
    'Saitou_424',
    'Takayasuhiro329',
    'hide_futakawa',
    'itsukihiguma',
    'akinobu593',
    'mayumi_ogawa',
    'ReiEnomoto',
    'KamadaYasuharu',
    'ELkDWoHH4sVMMD9',
    'MICHIEIMAI',
    'KHagi_Funabashi',
    'ochitatsuya0711',
    'okitsutokyo',
    'ImlILWLwgsC8Ufk',
    'tomohisa_tanaka',
    'kuroda__taro',
    'KikuchiDaijiro',
    'New__wind',
    'hiroyukishiman1',
    'daisuke_giin',
    'shyonchi',
    'shimazutetsuya6',
    'motoshimorii',
    'ishiguronerima',
    'koji_oashi',
    'nakataniayano',
    'Hashimoto_Mkhk',
    'kokuminhodo',
    'y_ishiwatari',
    'tomoyan_yoko',
    'hiro_0202aq',
    'nomuramiho3434',
    'Yamatake914',
    'Sukegawa_satoru',
    'okuda_shinichi',
    'Keisuke_Hamazoe',
    'jyano521',
    'oga1227',
    'kurokumagaya',
    'nkm27',
    'nakahi',
    'takayuki_ngsk',
    'MiyukiMatuda',
    'osunishiokades',
    'TokizakiNaoyuki',
    'maekawa190',
    'rurukisakamoto',
    'IwataHirotaka',
    'yukarikanetou',
    'kanetououentai',
    'kanetou55',
    'TWNapoli',
    'bunkyotaizo',
    'YumiYamaki107',
    'takazawa1',
    'NiheiFumitaka',
    'kajiwarahideki',
    'ryoma_mino',
    'Kawakita_Masaru',
    'satoakio310',
    'lpSaWpiOJwz6uqd',
    'G1i9olE3i1NIWsA',
    'BVd5wh9e90eA5mj',
    'junko_okano',
    'kokumin_kuma',
    'minshin_y',
    'dpj_kagoshima',
    't_kakuda',
    'gutsdego',
    'Ishida_shingo51',
    'kawai_akinari',
    'fukasakuyui',
    'yamanoitakashi',
    'taisuke_nkmr',
    'enoayu_minato',
    'Henry66239746',
    'hasegawa_takako',
    'miyahara_hiro',
    '_tanakaerika_',
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
    'minshuwakayama',
    'hamaoka_hiroki',
    'yukinumatautazu',
    'estakihabu',
    'hideo_ito',
    'h_ishizaki',
    'wako0501',
    'ShioriYamao',
    'FukasakuKj',
    'tannomidori',
    'tarui_yoshikazu',
    'tomoekakuda',
    'hide_usuki',
    'yoheiogawa_DPFP',
    'KzAGu2ES5XwFYUI',
    'yasuhirokogayu',
    'ouchi_kazuya',
    'mirailabo0913',
    'reiko_mtsmt',
    'suzukimiyuki701',
    'tomiyama_ka',
    'Miyagi_Suen',
    'kinno_takayasu',
    'umetsuyosei',
    'Shiro117385631',
    'one_ehime',
    'ksk_0910',
    'atsuko_call',
    'fxI8dS0hrIw6lyl',
    'Kisuzu_udon',
    'IwasakiIwamo',
    'inzai_mariko',
    'karuishi_y',
    'yumibetterworld',
    'maenomamiko',
    'maetsuyoshi',
    'kyoko_ohta',
    'Toru_Fukuta',
    'madokayoriko',
    'mariko_hichiwa',
    'shinju_nakayama',
    'yosshisuzuki',
    'tokita812',
    'hiro914',
    'katsuhikoasano',
    'suzuki_yuma1009',
    'DPFPnews',
    'tamakiyuichiro',
    'Maehara2016',
    'SHIMBA_OFFICE',
    'kouhei1005mon',
    'Fullgen',
    'itotakae0630',
    'Asano__Satoshi',
    'T_KAWAI_SANGIIN',
    'hamanoyoshifumi',
    'yasue_funayama0',
    'HamaMako0518',
    'IsozakiTetsuji',
    'Takezume_H',
    'mamitamuratw',
    'nagatomoshinji',
    'tanaka_shizuoka',
    'suzukiatsushi_',
    'AlexSaito2019',
}

members_list = []

for screen_name in user_list:
    print(screen_name)
    user = api.get_user(screen_name=screen_name)
    user_info = [user.name, '@' + user.screen_name, user.followers_count]
    print(user_info)
    if (user.description == '' and user.statuses_count != 0):
        members_list.append(user_info)


sorted_list = sorted(members_list, key=itemgetter(2), reverse=True)
print(*sorted_list, sep='\n')
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
                  'name', 'screen_name', 'followers_count'])
df.to_csv(dir + '/NoStatus_users_' +
          datetime.datetime.now().strftime('%y%m%d%H%M%S') + '.csv')
# removed_users.to_csv(dir + '/removed_users_' + datetime.datetime.now().strftime('%y%m%d%H%M%S') + '.csv')
