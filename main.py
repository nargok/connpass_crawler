import urllib.request
import json
import os
import time

os.makedirs('result', exist_ok=True)

search_term = ''
this_month = '202012'
next_month = '202101'
query_base = "https://connpass.com/api/v1/event/?ym=%s&ym=%s&keyword=%s"

def get_events():
    # TODO 後でループの対応をする
    # TODO  1秒ごとのwaitを入れて過剰アクセスを防止する
    query = query_base % (
        this_month, next_month, search_term
    )
    print(query)
    data = urllib.request.urlopen(query).read().decode("utf-8")
    response_json = json.loads(data)
    return response_json

def save_file(response_json):
    for event in response_json["events"]:
        filepath = "result/%d.json" % event["event_id"]
        fp = open(filepath, "w")
        fp.write(json.dumps(event, sort_keys=True, indent=2))
        fp.close()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    response_json = get_events()
    save_file(response_json)


