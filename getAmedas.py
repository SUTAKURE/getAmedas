import requests
#https://yuukiyg.hatenablog.jp/entry/2019/11/17/182410

#東京駅の緯度・経度
url = 'http://api.openweathermap.org/data/2.5/weather?' + \
       'lat=35.68'   + \ 　                      #緯度
       '&lon=139.77' + \                         #軽度
       '&APPID=9d22899629dc794d676cd815c925cad3' #APIkey

response = requests.get(url)
print(response.status_code)    # HTTPのステータスコード取得
print(response.text)    # レスポンスのHTMLを文字列で取得
