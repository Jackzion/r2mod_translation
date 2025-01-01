import requests
import hashlib
import random
import json
import time

app_key = 'xxxxxxxx'
app_secret = 'xxxxxxxx'
from_lang = 'en'
to_lang = 'zh-CHS'
def translate(query):
    try:
        salt = random.randint(1, 65536)
        sign = app_key + query + str(salt) + app_secret
        sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
        translation = 'not translation'

        url = 'https://openapi.youdao.com/api'
        params = {
            'q': query,
            'from': from_lang,
            'to': to_lang,
            'appKey': app_key,
            'salt': salt,
            'sign': sign
        }

        response = requests.get(url, params=params)
        result = response.json()
        if('translation' in result):
            translation_list = result['translation']
            translation = translation_list[0]
            print(translation)
        else:
            print(result)
        time.sleep(1)
    except Exception as e:
        print('fail to tranlate by api : ' + e)

    return translation;

