#-*-coding:utf-8-*-
import requests
import re
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

if __name__ == "__main__":
    headers={'User-Agent':USER_AGENT,
           }
    session = requests.Session()
    req = session.get('http://maoyan.com/board/4?offset=0',headers = headers, timeout = 5)
    compilestr = r'<dd>.*?<i class="board-index.*?<img data-src="(.*?)@.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">.*?(.*?)</p'
    #print(req.content)
    pattern = re.compile(compilestr,re.S)
    #print(req.content.decode('utf-8'))
    lists = re.findall(pattern,req.content.decode('utf-8'))
    for item in lists:
        #print(item)
        print(item[0].strip())
        print(item[1].strip())
        print(item[2].strip())
        print(item[3].strip())
        print('\n')
    
    
    
