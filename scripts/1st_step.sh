#!/usr/bin/bash

echo "イベントデータの取得を開始します"

rm result/*

python get_event_data.py

echo "イベントデータの取得が終了しました"
