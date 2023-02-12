import bs4
import requests
import textwrap
import time

# 全ページ分をリストにする


def get_all_reviews(url):
    rvw_list = []
    i = 1
    while True:
        print(i, 'searching')
        i += 1
        res = requests.get(url)
        amazon_soup = bs4.BeautifulSoup(res.text, features='lxml')
        rvws = amazon_soup.select('.review-text')
        for rvw in rvws:
            rvw_list.append(rvw)

        # 次へボタン
        next_page = amazon_soup.select('li.a-last a')

        if next_page != []:
            next_url = 'https://www.amazon.co.jp/' + next_page[0].attrs['href']
            url = next_url
            # 最低でも1秒は間隔をあける
            time.sleep(1)
        else:
            break

    return rvw_list


if __name__ == '__main__':

    # 　Amzon商品ページ
    url = 'https://www.amazon.co.jp/%E6%89%8B%E6%8C%87%E6%B6%88%E6%AF%92%E5%89%A4%E3%80%91%E3%83%8F%E3%83%B3%E3%83%89%E3%82%B9%E3%82%AD%E3%83%83%E3%82%B7%E3%83%A5EX-%E3%81%A4%E3%81%91%E3%81%8B%E3%81%88%E7%94%A8-800ml-%E8%8A%B1%E7%8E%8B%E3%83%97%E3%83%AD%E3%83%95%E3%82%A7%E3%83%83%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-%E6%8C%87%E5%AE%9A%E5%8C%BB%E8%96%AC%E9%83%A8%E5%A4%96%E5%93%81/dp/B005RUI15O/'

    # URLをレビューページのものに書き換える
    new_url = url.replace('dp', 'product-reviews')
    # レビューの取得
    rvw_list = get_all_reviews(new_url)

    # 全データを表示
    for i in range(len(rvw_list)):
        rvw_text = textwrap.fill(rvw_list[i].text, 80)
        print('\nNo.{} : '.format(i+1))
        print(rvw_text)
