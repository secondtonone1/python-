#-*-coding:utf-8-*-
import requests
import http.cookiejar, urllib.request
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
COOKIE = '_zap=860b3564-8750-4f74-884e-92bbb9889f37; \
        d_c0="AJDmouQjGA6PTqTesVKUeMhrpmJrMi3h1tM=|1534918190"; \
        z_c0="2|1:0|10:1534918318|4:z_c0|92:Mi4xSk5RdUFBQUFBQUFBa09haTVDTVlEaVlBQUFCZ0FsVk5ya3hxWEFEa0NQVE1zN2lwV3dMUVFkOUFibXZiLWFDbnBB|5966970bc1d119762840fe73362b19cf2948b850a23cdbd2ed42150bd585ecc6";\
        __gads=ID=5caca3053cdd5eba:T=1539584288:S=ALNI_Mag94pZSq3q7hiGNXtlhiaxpY-Htw; q_c1=de34732dc90a4c77b370861f34a7a2b1|1540950273000|1534918191000;\
        __utma=51854390.1155392069.1535089086.1540534370.1540950265.5;\
        __utmz=51854390.1540950265.5.5.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/;\
        __utmv=51854390.100-1|2=registration_date=20140113=1^3=entry_date=20140113=1; _xsrf=86f079c3-df1a-456f-9da8-d3adc7b52a50;\
        tst=r; tgw_l7_route=200d77f3369d188920b797ddf09ec8d1'
if __name__ == "__main__":
    headers={'User-Agent':USER_AGENT,
            'Host':'www.zhihu.com',
            'Cookie':COOKIE}
    req = requests.get('https://www.zhihu.com',headers=headers,timeout=5)
    print(req.text)

