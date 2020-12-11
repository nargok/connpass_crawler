# README

IT勉強会サイト[connpass](https://connpass.com/) のイベント情報を取得してCSVデータを作成するスクリプトです。

## 事前準備
python環境の設定
```
python3 -m venv venv
source venv/bin/activate
```

ライブラリのダウンロード
```
pip install -r requirements.txt
```

## 処理実行手順
イベントデータのダウンロード
```
sh scripts/1st_step.sh
```

CSVファイルの作成
```
sh scripts/2nd_step.sh
```