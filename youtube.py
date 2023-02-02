from googleapiclient.discovery import build

YOUTUBE_API_KEY = 'AIzaSyBAQ2x7r2GTR_ESWC13amJkG5VmSBOu3uI'

user_list = {
    'UCJc_jL0yOBGychLgiTCGtPw',
    'UCRvoO9oxJBhHAIvevzSJT3w',
    'UCLJNZ7osIjNix4bbkM-rj5w',
    'UCMG5j9U1wI2m_fH3ThLhVZw',
    'UCmPZG_kOdGb7XAI7J0JBeMQ',
    'UCn5YaIkKPivHCvnITBzOYcg',
    'UCFQuI8XeyiUE4znVZwTt5Sw',
    'UCjtBv-OYlFveoIKwJrGE3lQ',
    'UCPyFaCFzmr4UXlJmg4RJBnQ',
    'UCdKVQYyUF9v2-XEB8HCUiiw',
    'UCf3A22QLymL2ePXVFgP8ukA',
    'UC4qf13hSUIA2HUDQ7N5jRVw',
    'UCzYiBNKmAWioIDUxLeTUO-Q',
    'UCRn4NRJ4eb1qukGApi03txQ',
    'UCUSoNPiQPElLtvqRusjD4dQ',
    'UCX_1oOPk1HtKL2K5DIl4pyw',
    'UCl-gLUuQWI2qRSsVUnRpXLA',
    'UCJCXqehY85HuNJGYXqw4IdA',
    'UCCMRYg5aiE3w0-5-bRV1DXQ',
    'UC437QZb3F0gnZWGgRPT0DEw',
    'UC_n4zO8_iy2oVOOttWfcZgQ',
    'UCXDbwIbzTK4U8xzkrbFDk4Q',
    'UCvI1UxQ949yS_mCjDqmG9wA',
    'UCXPDzLCesIIYZZDb0UphOWw',
    'UC4yP_T0KyIc7OR7nWgPHtAw',
    'UCgX_iJmfXY8H8q803NTqWKA',
    'UCCD_gofOdJnUXTeFvxFln1A',
    'UCrd4q1X65ZZdQAEc1iQ0nhg',
    'UCywRrysecQibw-yA9WD2qBQ',
    'UC1U6AhGYSD3qcXlk1Y9v-_Q',
    'UCuXrocorVtSXcodJ8P0aHrQ',
    'UCdeZ9kSZBi38z_BgWCFbx3w',
    'UC2iT6lhfuIEK23R1LFuLbkw',
    'UC29Vz-CJneDCQZHlcxAit-A',
    'UCp5ZGRS2WZujP3Oi2C3Kquw',
    'UCmSDOi2DMMmnBXAMOssIfAg',
    'UC_BZLxCt_gvQl_gq_-ttwDA',
    'UCgjS2ANA7hz6Hc19qFdcbHw',
    'UCa3gqzsYYwdfkgST-C9SbIg',
    'UCzMYAD6mn_S8lI4EfQ4qGtw',
    'UC88peYfCbtZD_J1DnkV57Rw',
    'UCbH8kZWzf-V1mxnwiAxLiBQ',
    'UCKYypEwgZFnQ58VFkb9I8SA',
    'UCbV1rhTQ2BttwpC8iBcONRA',
    'UCRKj50BisTKn4Cl2LgP4z5Q',
    'UC-gXxlofqLp-Hg6NbZlimqQ',
    'UCBUIAUGv2iJyCI6Uy_U9goQ',
    'UCZD-_dVdmzMZmo9UpSHntRA',
    'UCW5YHEu7mZLKbsp9y1SmZKQ',
    'UCdHrvhJTXxl9ynb2M528YrQ',
    'UCxQ1vvDTvlW8Ul-vt7LbfgQ',
    'UCE4ANmWn0YqTGr7R9Mj3RpA',
    'UC0XUX5rqtXhd4akCHm0r3Sg',
    'UCZXaGH1h6LLsaz1WXvLBOgg',
    'UCmVny-y_G62dQw7EGYFnL0g',
    'UC3szSM2Pox_jmXU5PlTZGQQ',
    'UCtmF4q2BBuXUNGWi4QQoA5A',
    'UCaNq0TOmm63MtMU_NfzxlCQ',
    'UCBJQK03FeDhl73fcqrVq3qw',
    'UCQURPnBnPDhgT6uXgWbizjg',
    'UC6_dVlZGpJlbvKEUznFVvbA',
    'UC8sRo4BSCgsP0O85trRNOwg',
    'UCSQa2VESBRPGV7y4gQeddQA',
    'UC91-sxK4nEvUt8yNRbbpaKQ',
    'UChqvAF0OZIvdzUaxqLH6Epg',
    'UCnUltJHRdMm4_peIdRbRI_Q',
    'UC-iWuuPSuSbB-AwOyFrs_cQ',
}

members_list = []

def youtube_channel_detail(channel_id, api_key):
    # print('youtube_channel_detail')
    api_service_name = 'youtube'
    api_version = 'v3'
    youtube = build(api_service_name, api_version, developerKey=api_key)
    print(channel_id)
    search_response = youtube.channels().list(
        part='snippet,statistics',
        id=channel_id,
    ).execute()

    # print(search_response)
    return search_response['items'][0]

# print('main')
for channel_id in user_list:
    d = youtube_channel_detail(channel_id, YOUTUBE_API_KEY)
    # print(d)
    # print(d['snippet']['title'])
    # print(d['snippet']['description'])
    # print('https://www.youtube.com/' + d['snippet']['customUrl'])
    # print('作成日: ' + d['snippet']['publishedAt'])
    # print('チャンネル登録者数: ' + d['statistics']['subscriberCount'])
    # print('視聴回数: ' + d['statistics']['viewCount'])
    # print('動画件数: ' + d['statistics']['videoCount'])
    # print('')
    detail_info = [d['snippet']['title'], 
        'https://m.youtube.com/' + d['snippet']['customUrl'], 
        'id: ' + d['id'],
        '作成日: ' + d['snippet']['publishedAt'],
        int(d['statistics']['subscriberCount']),
        '視聴回数: ' + d['statistics']['viewCount'],
        '動画件数: ' + d['statistics']['videoCount']]
    # print(d)
    members_list.append(detail_info)

from operator import itemgetter

# print(members_list)

sorted_list = sorted(members_list, key=lambda x:x[4], reverse=True)
# print(type(int(sorted_list[0][3])))
# print(*sorted_list, sep='\n')

for d in sorted_list:
    print(d[0])
    print(d[1])
    print(d[2])
    print(d[3])
    print('チャンネル登録者数: ' + str(d[4]))
    print(d[5])
    print(d[6])
    print('')
