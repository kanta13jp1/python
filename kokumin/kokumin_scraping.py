import bs4
import requests
import textwrap
import time
import pymongo

# 全ページ分をリストにする


def get_all_reviews(url):
    rvw_list = []
    i = 1
    while True:
        print(i, 'searching')
        i += 1
        res = requests.get(url)
        # print(res.text)
        amazon_soup = bs4.BeautifulSoup(res.text, features='html.parser')
        print(type(amazon_soup))
        # print(amazon_soup)
        rvws = amazon_soup.select('a')
        print(type(rvws))
        for rvw in rvws:
            # print(rvw.find('span'))
            while (rvw.find('span') != None):
                rvw.find('span').extract()
            # print(rvw.getText())
            # print(type(rvw))
            if (rvw.getText().find('投開票') != -1):
                rvw_list.append(rvw)
        # print(rvw_list)
        # print(len(rvw_list))
        # # 次へボタン
        # next_page = amazon_soup.select('li.a-last a')

        # if next_page != []:
        #     next_url = 'https://www.amazon.co.jp/' + next_page[0].attrs['href']
        #     url = next_url
        #     # 最低でも1秒は間隔をあける
        #     time.sleep(1)
        # else:
        #     break
        break

    return rvw_list


if __name__ == '__main__':

    # 　Amzon商品ページ
    # url = 'https://www.amazon.co.jp/%E6%89%8B%E6%8C%87%E6%B6%88%E6%AF%92%E5%89%A4%E3%80%91%E3%83%8F%E3%83%B3%E3%83%89%E3%82%B9%E3%82%AD%E3%83%83%E3%82%B7%E3%83%A5EX-%E3%81%A4%E3%81%91%E3%81%8B%E3%81%88%E7%94%A8-800ml-%E8%8A%B1%E7%8E%8B%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-%E6%8C%87%E5%AE%9A%E5%8C%BB%E8%96%AC%E9%83%A8%E5%A4%96%E5%93%81/dp/B005RUI15O/'
    url = 'https://new-kokumin.jp/election'

    # URLをレビューページのものに書き換える
    new_url = url.replace('dp', 'product-reviews')
    # レビューの取得
    print(new_url)
    rvw_list = get_all_reviews(new_url)
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["test"]
    mycol = mydb["test"]
    # f = open('myfile.txt', 'w', encoding='UTF-8')
    # DBのデータを削除
    x = mycol.delete_many({})
    print(x.deleted_count, " documents deleted.")
    # 全データを表示
    for i in range(len(rvw_list)):
        rvw_text = textwrap.fill(rvw_list[i].text, 80)
        # print('\nNo.{} : '.format(i+1))
        # f.write('\nNo.{} : '.format(i+1))
        # f.write('\n')
        # print(rvw_text)
        # print(rvw_text.replace('     ', '').replace(
        #     '  ', '\n').replace(' 2', '\n 2').replace('票 ', '票\n '))
        # f.write(rvw_text.replace('     ', '').replace(
        #     '  ', '\n').replace(' 2', '\n 2').replace('票 ', '票\n '))
        # f.write('\n')
        data = rvw_text.replace('     ', '').replace(
            '  ', '\n').replace(' 2', '\n 2').replace('票 ', '票\n ')
        mydict = {"No": format(i+1), "data": data}
        print(mydict)
        x = mycol.insert_one(mydict)
        print(x)
    # f.close()
