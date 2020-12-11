import glob
import json
import pandas
import pandas.io.json

event_list = []


def read_json_files(events):
    for filename in glob.glob("result/*.json"):
        event = json.loads(open(filename).read())
        events.append(event)

    return events


def save_csv(events):
    df = pandas.json_normalize(events)

    csv_data = df.to_csv()
    csv_data = csv_data.encode("cp932", "ignore")

    fp = open('connpass_result.csv', "wb")
    fp.write(csv_data)

    fp.close()

if __name__ == '__main__':
    print('hi')
    event_list = read_json_files(event_list)
    save_csv(event_list)



