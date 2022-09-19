# coding = utf8
# author
# 恋恋风辰
import requests
import random
import os
import logging
from concurrent.futures import ThreadPoolExecutor,as_completed
import threading
import time

class SheepUpdate:
    def __init__(self, token):
        headers = {
        'Host': 'cat-match.easygame2021.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.28(0x18001c27) NetType/WIFI Language/zh_CN',
        't': token,
        'Referer': 'https://servicewechat.com/wx141bfb9b73c970a9/17/page-frame.html',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'Connection': 'close',
        }
        self.headers = headers
        cur_dir = os.path.dirname(__file__)
        log_path = os.path.join(cur_dir, "example.log")
        logging.basicConfig(filename='info.log', level=logging.DEBUG, encoding='utf-8')
        print(log_path)
        print("羊了个羊")

    #每日话题加入羊群
    def join_sheep(self):
        url = f"https://cat-match.easygame2021.com/sheep/v1/game/topic_game_over?rank_score=1&rank_state=1&rank_time={random.randint(1, 3600)}&rank_role=1&skin=1"
        res = requests.get(url,headers=self.headers)
        print(res.text)
    
    #更新通关次数
    def update_res(self, count=1,seconds=0):
        time.sleep(seconds)
        response = requests.get(
            f'https://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_time={random.randint(1, 3600)}&rank_role=1&skin=1', headers=self.headers, timeout=10, verify=True)
        if response == None:
            print("response is none")
            logging.info("response is none")
            return f'task {count} failed'
        if response.json()['err_code'] == 0:
            print(f'执行任务:{count}成功')
            logging.info(f'执行任务:{count}成功')
            return f'task {count} success'
        else:
            print(f'失败, 返回内容为:\n{response.json()}')
            logging.info(f'failed, reason is :\n{response.json()}')
            return f'task {count} failed'

    def update_res_batch(self, count):
        pool = ThreadPoolExecutor(max_workers=5)
        all_tasks = []
        for index in range(count):
            all_tasks.append(pool.submit(self.update_res,index+1,1))
        for future in as_completed(all_tasks):
            data = future.result()
            print("task done, result is {}".format(data))
            logging.info("task done, result is {}".format(data))
            pass
        pool.shutdown()

if __name__ == "__main__":
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ1MDY5ODEsIm5iZiI6MTY2MzQwNDc4MSwiaWF0IjoxNjYzNDAyOTgxLCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJvcGVuX2lkIjoiIiwidWlkIjo2ODIwNTE1NCwiZGVidWciOiIiLCJsYW5nIjoiIn0.dhjSA7U9zqxblbceN0vuyu736o53JmT7rTucJywtsrs"
    #SheepUpdate(token).update_res()
    #SheepUpdate(token).update_res_batch(20)
    SheepUpdate(token).join_sheep()
    pass