import struct
import base64
import requests
 
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.28(0x18001c27) NetType/WIFI Language/zh_CN',
    #'t': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ1MDY5ODEsIm5iZiI6MTY2MzQwNDc4MSwiaWF0IjoxNjYzNDAyOTgxLCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJvcGVuX2lkIjoiIiwidWlkIjo2ODIwNTE1NCwiZGVidWciOiIiLCJsYW5nIjoiIn0.dhjSA7U9zqxblbceN0vuyu736o53JmT7rTucJywtsrs",
    't':"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ2NzY4NjAsIm5iZiI6MTY2MzU3NDY2MCwiaWF0IjoxNjYzNTcyODYwLCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJvcGVuX2lkIjoiIiwidWlkIjo2ODAwODQ4NiwiZGVidWciOiIiLCJsYW5nIjoiIn0.RjhpCKVFexinSU64UmoaW5th90qqaomnCtPLBmpNQhY",
    'Referer': 'https://servicewechat.com/wx141bfb9b73c970a9/23/page-frame.html'
 
}
url = 'https://cat-match.easygame2021.com/sheep/v1/game/personal_info?'
r = requests.get(url, headers=headers)
print(r.json())
url = 'https://cat-match.easygame2021.com/sheep/v1/game/map_info_ex?matchType=3'
r = requests.get(url, headers=headers)
map_md5 = r.json()['data']['map_md5'][1]
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
MatchPlayInfo = base64.b64encode(data).decode('utf-8')
print(MatchPlayInfo)
url = 'https://cat-match.easygame2021.com/sheep/v1/game/game_over_ex?'
r = requests.post(url, headers=headers,json={'rank_score': 1, 'rank_state': 1, 'rank_time': 1, 'rank_role': 1, 'skin': 1,'MatchPlayInfo': MatchPlayInfo})
print(r.json())
url = 'https://cat-match.easygame2021.com/sheep/v1/game/personal_info?'
r = requests.get(url, headers=headers)
print(r.json())