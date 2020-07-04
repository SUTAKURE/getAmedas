import requests
import ast
#https://yuukiyg.hatenablog.jp/entry/2019/11/17/182410

# 東京駅の緯度・経度
url = 'http://api.openweathermap.org/data/2.5/weather?' + \
       'lat=35.68'   + \
       '&lon=139.77' + \
       '&APPID=9d22899629dc794d676cd815c925cad3'

# openwethermapから天気情報を取得
response = requests.get(url)
dic = ast.literal_eval(response.text)
print(dic['coord'])   #座標
print(dic['weather']) #天気の様子
print(dic['main'])    #天気概観
print(dic['sys'])     #天気概観
print(dic['name'])    #取得場所
