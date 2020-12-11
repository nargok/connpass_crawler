import time
import urllib
import urllib.request
import os
import datetime
import json
import readline
from dateutil.relativedelta import relativedelta

os.makedirs('result', exist_ok=True)
query_base = "https://connpass.com/api/v1/event/?ym=%s&ym=%s&keyword=%s&count=%d&start=%d"
INITIAL_DATA_POSITION = 1
DATA_SIZE = 10
parameter_base = "(当月: %s 次月: %s キーワード: %s サイズ: %d件 開始位置: %d)"


def get_search_range():
    today = datetime.date.today()
    from_month = today.strftime('%Y%m')
    to_month = (today + relativedelta(months=1)).strftime('%Y%m')

    return from_month, to_month


def save_file(response):
    for event in response["events"]:
        filepath = "result/%d.json" % event["event_id"]
        fp = open(filepath, "w")
        fp.write(json.dumps(event, sort_keys=True, indent=2))
        fp.close()


def get_events(this_month, next_month, keyword):
    data_position = INITIAL_DATA_POSITION
    for i in range(5):
        keyword_quote = urllib.parse.quote(keyword)
        try:
            query = query_base % (
                this_month, next_month, keyword_quote, DATA_SIZE, data_position
            )
            parameter = parameter_base % (
                this_month, next_month, keyword, DATA_SIZE, data_position
            )
            print('以下の条件でイベント情報をダウンロードします')
            print(parameter)

            data = urllib.request.urlopen(query).read().decode("utf-8")
            json_data = json.loads(data)
        except:
            break

        save_file(json_data)
        data_position += DATA_SIZE

        time.sleep(1)


if __name__ == '__main__':
    month1, month2 = get_search_range()
    input_val = input('検索したいイベントのキーワードを入力ください\n※未入力でも大丈夫です\n')
    get_events(month1, month2, input_val)


