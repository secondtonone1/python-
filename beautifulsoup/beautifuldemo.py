#-*-coding:utf-8-*-
import requests
import re
import time
from lxml import etree
from bs4 import BeautifulSoup


if __name__ == "__main__":
    #html = '''div id="sslct_menu" class="cl p_pop" style="display: none;">
    #<span class="sslct_btn" onClick="extstyle('')" title="默认"><i></i></span></div>
    #<ul id="myitem_menu" class="p_pop" style="display: none;">
    #<li><a href="https://www.aisinei.org/forum.php?mod=guide&amp;view=my">帖子</a></li>
    #<li><a href="https://www.aisinei.org/home.php?mod=space&amp;do=favorite&amp;view=me">收藏</a></li>'''
    #bs = BeautifulSoup(html)
    #print(bs.prettify())
   # s =BeautifulSoup('test.html','lxml')
    #print(s.prettify())
    
    html2 = ''' <li class="bus_postbd item masonry_brick">
	<div class="bus_vtem">
		<a href="https://www.aisinei.org/thread-17846-1-1.html" title="XIUREN秀人网 2018.11.13 NO.1228 猫宝 [50+1P]" class="preview"  target="_blank">
		hello world
        <img src="https://i.asnpic.win/block/a4/a42e6c63ef1ae20a914699f183d5204b.jpg" width="250" height="375" alt="XIUREN秀人网 2018.11.13 NO.1228 猫宝 [50+1P]"/>
                ss2<span class="bus_listag">XIUREN秀人网</span>
		</a>
		<a href="https://www.aisinei.org/thread-17846-1-1.html" title="XIUREN秀人网 2018.11.13 NO.1228 猫宝 [50+1P]"  target="_blank">
			<div class="lv-face"><img src="https://www.aisinei.org/uc_server/avatar.php?uid=2&size=small" alt="发布组小乐"/></div>
			<div class="t">XIUREN秀人网 2018.11.13 NO.1228 猫宝 [50</div>
			<div class="i"><span><i class="bus_showicon bus_showicon_v"></i>6402</span><span><i class="bus_showicon bus_showicon_r"></i>1</span></div>
		</a>
	</div>
	</li> '''
    s2 = BeautifulSoup(html2,'lxml')
    #print(s2.li)
    #print(s2.a)
    #print(s2.a.name)
    #print(s2.a.attrs)
    #print(s2.a.string)
    #print(s2.a.text)
    #print(s2.div.contents)
    #print(s2.div.children)
    #print(s2.div.contents[0])
    #for i in s2.div.children:
        #print(i)
    #print(s2.div)
    #print(s2.a["href"])
    #print(s2.a.get("href"))
    '''
    #孙子节点
    print(s2.div.descendants)
    #祖先节点
    print(s2.div.parents)
    #直接父节点
    print(s2.div.parent)
    #下一个兄弟节点
    print(s2.a.next_sibling)
    #前一个兄弟节点
    print(s2.a.previous_sibling)
    print(s2.find('a'))
    print(s2.find_all('a'))
    print(s2.find_all(re.compile("^div")))
    print(s2.find_all(["div","li"]))
    '''
    #查找节点为div的数据
    print(s2.select('a'))
    #查找class为bus_vtem的节点
    print(s2.select('.bus_vtem'))
    #查找id为ps的节点
    print(s2.select('#ps'))

    
    
    
