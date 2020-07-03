# -*- coding: utf-8 -*-

import requests, json
TOKEN = 'ここには自分のアカウントのトークンを貼り付ける'
def get_amedas_1min(year, month, day, hour, minute, payload={}):
    """
    /api/v1/amedas/1minを実行
    Parameters
    ----------
    year : string
        西暦年 (4桁の数字で指定) UTC
    month : string
        月 01～12 (2桁の数字で指定) UTC
    day : string
        日 01～31 (2桁の数字で指定) UTC
    hour : string
        時 00～23 (2桁の数字で指定) UTC
    minute : string
        分 00～59 (2桁の数字で指定) UTC
    payload : dict
        パラメータ(min_lat,min_lon,max_lat,max_lon)
    Returns
    -------
    content : list
        結果
    """

    url = 'https://gisapi.tellusxdp.com/api/v1/amedas/1min/{}/{}/{}/{}/{}/'.format(year, month, day, hour, minute)
    headers = {
        'Authorization': 'Bearer ' + TOKEN
    }
    r = requests.get(url, headers=headers, params=payload)
    if r.status_code != 200:
        print(r.content)
        raise ValueError('status error({}).'.format(r.status_code))
    return json.loads(r.content)

amedas1 = get_amedas_1min('2015', '12', '31', '15', '01')
print(len(amedas1))
print(amedas1[0])
