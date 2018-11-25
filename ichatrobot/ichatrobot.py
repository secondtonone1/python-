# coding = utf8
import requests
import itchat
# 去图灵机器人官网注册后会生成一个apikey，可在个人中心查看
KEY = '7fbcf063ce2f46eab0a224b6e988cb47'
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'   : KEY,
        'info'   : msg,   # 这是要发送出去的信息
        'userid'  : 'wechat-rebot',  #这里随意写点什么都行
    }
    try:
        # 发送一个post请求
        r = requests.post(apiUrl, data =data).json()
        # 获取文本信息，若没有‘Text’ 值，将返回Nonoe 
        return r.get('text')
    except:
        return
# 通过定义装饰器加强函数 tuling_reply(msg) 功能，获取注册文本信息
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 设置一个默认回复，在出现问题仍能正常回复信息
    #defaultReply = 'I received: ' +msg['Text']
    defaultReply ='有事在忙，回聊!'
    reply = get_response(msg['Text'])
    # a or b 表示，如有a有内容，那么返回a，否则返回b
    return reply or defaultReply

       
if __name__ == "__main__":
    # 使用热启动，不需要多次扫码
    itchat.auto_login(hotReload=True)
    itchat.run()

   
    
    
    
    
