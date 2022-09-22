# coding = utf8
# author
# 恋恋风辰
from math import fabs
import requests
import random
import os
import logging
from concurrent.futures import ThreadPoolExecutor,as_completed
import threading
import time
from requests import Session
from requests.packages import urllib3
import struct
import base64
class SheepUpdate:
    def __init__(self, token):
        headers = {
        'Host': 'cat-match.easygame2021.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.28(0x18001c27) NetType/WIFI Language/zh_CN',
        't': token,
        'Referer': 'https://servicewechat.com/wx141bfb9b73c970a9/24/index.html',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'Connection': 'close',
        }
        self.headers = headers
        self.session = Session()
        self.MatchPlayInfo = ""
        cur_dir = os.path.dirname(__file__)
        log_path = os.path.join(cur_dir, "info.log")
        logging.basicConfig(filename=log_path, level=logging.DEBUG, encoding='utf-8')
        print(log_path)
        print("羊了个羊")

    #获取token
    def get_info(self):
        url = 'http://cat-match.easygame2021.com/sheep/v1/game/personal_info?'
        r = requests.get(url, headers=self.headers, verify=False)
        print(r.json())
      

    #每日加入羊群
    def join_sheep(self):
        url = 'https://cat-match.easygame2021.com/sheep/v1/game/game_over_ex?'
        r = requests.post(url, headers=self.headers,json={'rank_score': 1, 'rank_state': 1, 'rank_time': random.randint(1, 3600), 'rank_role': 1, 'skin': 1,'MatchPlayInfo': self.MatchPlayInfo})
        print(r.json())
    


    #获取地图
    def get_map(self):
        url = f"http://cat-match.easygame2021.com/sheep/v1/game/map_info_ex?matchType=3"
        res = requests.get(url,headers=self.headers)
        print(res.text)
        map_md5 = res.json()['data']['map_md5'][1]
        url = f'https://cat-match-static.easygame2021.com/maps/{map_md5}.txt'  # 由于每天获取的地图不一样，需要计算地图大小
        r = requests.get(url)
        levelData = r.json()['levelData']
        p = []
        for h in range(len(sum(levelData.values(), []))):  # 生成操作序列
            p.append({'chessIndex': 127 if h > 127 else h, 'timeTag': 127 if h > 127 else h})
        GAME_DAILY = 3
        GAME_TOPIC = 4
        data = struct.pack('BB', 8, GAME_DAILY)
        for i in p:
            c, t = i.values()
            data += struct.pack('BBBBBB', 34, 4, 8, c, 16, t)
        self.MatchPlayInfo = base64.b64encode(data).decode('utf-8')
        print(self.MatchPlayInfo)

if __name__ == "__main__":
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQwNzE2MzUsIm5iZiI6MTY2MzgxMzIzNSwiaWF0IjoxNjYzODExNDM1LCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJ1aWQiOjEyMjk0NjY1OCwidmVyIjoiMSIsImV4dCI6IjM2MzMzMjYyNjI2MzM5MzMzOTMzNjEzMjY0Mzk2NjY0NjM2NTY2MzIzODY1MzQzMSIsImNvZGUiOiJlNjUwMDE1NzEzNGUxYmViZjEwZmMyYzZiMjY1M2MxNiIsImVuZCI6MTY2NDA3MTYzNTcxM30.QryLUGjOFBL7jtQvnShB-xX0eZY_m-oYHkLLdi9VmlI"
    urllib3.disable_warnings()
    SheepUpdate(token).get_map()
    SheepUpdate(token).join_sheep()
    SheepUpdate(token).get_info()