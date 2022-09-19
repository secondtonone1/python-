import requests

headers = {
    "user-agent":"Mozilla/5.0 (Linux; Android 10; HD1910 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4309 MMWEBSDK/20220303 Mobile Safari/537.36 MMWEBID/583 MicroMessenger/8.0.21.2120(0x280015F0) Process/appbrand1 WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64 MiniProgramEnv/android"
}

#获取基本信息
def user_info(uid):
    url = "https://cat-match.easygame2021.com/sheep/v1/game/user_info?"
    params = {
        "uid":uid,
        "t":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ0MDU0MjMsIm5iZiI6MTY2MzMwMzIyMywiaWF0IjoxNjYzMzAxNDIzLCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJvcGVuX2lkIjoiIiwidWlkIjoxMDg0MzMxMjgsImRlYnVnIjoiIiwibGFuZyI6IiJ9.oT1OY9XokZmHt1Hzifc8ILF1U-xQxY-itXNaeLj02R8"
    }
    res = requests.get(url,params=params).json()["data"]
    return res

#获取token
def get_token(uid):
    user = user_info(uid)
    url = "https://cat-match.easygame2021.com/sheep/v1/user/login_oppo"
    data = {
        "uid":user["wx_open_id"],
        "nick_name": user["nick_name"],
        "avatar":user["avatar"],
        "sex" : 1
    }
    res = requests.post(url,data=data,headers=headers).json()['data']['token']
    return res

#每日话题加入羊群
def join_sheep():
    url = "https://cat-match.easygame2021.com/sheep/v1/game/topic_game_over?rank_score=1&rank_state=1&rank_time=1&rank_role=1&skin=1"
    res = requests.get(url,headers=headers)
    print(res.text)

#刷通关次数
def game_over():
    url = "https://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_time=1&rank_role=1&skin=1"
    res = requests.get(url,headers=headers)
    print(res.text)

if __name__ == '__main__':

    token = get_token('xxxxxxx') #填写你自己的uid
    headers['t'] = token
    join_sheep()
    game_over()