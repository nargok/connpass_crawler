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


def change_timestamp_type(df):
    # 末尾が_atのカラムをdatetime型に変換する
    datetime_columns = filter(lambda a: a[-3:] == '_at', df.columns)
    for column in datetime_columns:
        df[column] = pandas.to_datetime(df[column], unit='s')

    return df


def save_csv(events):
    df = pandas.json_normalize(events)

    # datetimeの変換 Unix Timestamp型で日時がくるものについてはこの変換処理をする
    # df = change_timestamp_type(df)

    csv_data = df.to_csv()
    csv_data = csv_data.encode("cp932", "ignore")

    fp = open('connpass_result.csv', "wb")
    fp.write(csv_data)

    fp.close()


if __name__ == '__main__':
    event_list = read_json_files(event_list)
    save_csv(event_list)
