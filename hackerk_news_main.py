"""
1.リクエストを送る

2.記事をとってくる
  トップ5の記事の情報をとってくる



"""
import requests


def send_query():  # リクエスト送るよ！！
    URL_TOTAL = ' https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
    total_id = requests.get(URL_TOTAL).json()
    # print(type(total_response))
    # print(total_response)
    ids = total_id[0:5]

    for id in ids:
        URL_TOP5 = f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty'
        top5_response = requests.get(URL_TOP5).json()
        print(top5_response['title'])
        print(top5_response['url'])
        print()


def main():
    send_query()


print("現在のTOP5の記事です。>")

if __name__ == '__main__':
    main()
