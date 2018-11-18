#-*-coding:utf-8-*-
import requests
import re
import time
from lxml import etree


if __name__ == "__main__":
    text = '''
    <div class="bus_vtem">
		<a href="https://www.aisinei.org/thread-17826-1-1.html" title="XINGYAN星颜社 2018.11.09 VOL.096 唐思琪 [47+1P]" class="preview"  target="_blank">
		<img src="https://i.asnpic.win/block/74/74eab64cfa4229d58c19a64970368178.jpg" width="250" height="375" alt="XINGYAN星颜社 2018.11.09 VOL.096 唐思琪 [47+1P]"/>
                <span class="bus_listag">XINGYAN星颜社</span>
		</a>
		<a href="https://www.aisinei.org/thread-17826-1-1.html" title="XINGYAN星颜社 2018.11.09 VOL.096 唐思琪 [47+1P]"  target="_blank">
			<div class="lv-face"><img src="https://www.aisinei.org/uc_server/avatar.php?uid=2&size=small" alt="发布组小乐"/></div>
			<div class="t">XINGYAN星颜社 2018.11.09 VOL.096 唐思琪 </div>
			<div class="i"><span><i class="bus_showicon bus_showicon_v"></i>5401</span><span><i class="bus_showicon bus_showicon_r"></i>1</span></div>
		</a>
	</div>
    '''

    html = etree.HTML(text)
    result = etree.tostring(html)
    #打印lxml生成的字符串，如果html格式不全，会自动补全
    #print(result.decode('utf-8'))
    # 打印根节点下所有子孙节点
    result2 = html.xpath('//*')
    #print(result2)
    result3 = html.xpath('//a[@class="preview"]')
    print(result3)
    result4 = html.xpath('//a[@class="preview"]/../@class')
    print(result4)
    text2 = '''
        <div class="bus_vtem  mtest"> hurricane!
        </div>
    '''
    html2 = etree.HTML(text2)    
    result5 = html2.xpath('//*[contains(@class, "mtest")]')
    # 错误用法
    #result5 = html.xpath('//*[@class="mtest"]')
    print(result5)

    text3 = '''
        <div class="bus_vtem mtest" name="hurricane"> hurricane!
        </div>
        <div class="bus_vtem mtest" name = "tornado"> tornado!
        </div>
    '''
    html3 = etree.HTML(text3)    
    result6 = html3.xpath('//*[contains(@class, "mtest") and @name="hurricane"]/text()')
    print(result6)
    
    
