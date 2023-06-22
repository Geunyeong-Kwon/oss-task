import streamlit as st
import pandas as pd
import json
import urllib.request

key = 'KU4sbUhkqLCoOaTz0eNuf5DBCORUzbcL7XaHhqi4qSY2%2Bs%2FFvwIGBBiG4tbIxRI%2F1ftQTPvmeQstoiwXt4I2tw%3D%3D'
url = 'http://apis.data.go.kr/1352000/ODMS_STAT_24/callStat24Api' + key + http://apis.data.go.kr/1352000/ODMS_STAT_24
json_page = urllib.request.urlopen(url)
json_data = json_page.read().decode("utf-8")
json_array = json.loads(json_data)

print(json_array)
