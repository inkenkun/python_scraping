# -*- coding:utf-8 -*-

import re
import urllib2

# BeautifulSoup ３系を使う場合
#from BeautifulSoup import BeautifulSoup

# BeautifulSoup ４系を使う場合
from bs4 import BeautifulSoup

### UAを設定
opener = urllib2.build_opener()
opener.addheaders=[
    ('User-Agent', "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36"),
    ('Accept-Language','ja,en-us;q=0.7,en;q=0.3')
]
urllib2.install_opener(opener)

url =  "http://www.mizuhobank.co.jp/takarakuji/loto/loto7/index.html"
soup = BeautifulSoup(urllib2.urlopen(url).read())

#回数
table = soup.findAll("table")[0]
regex = u'第(.*?)回'
kuji_id = re.search(regex, unicode(table)).group(1)

#日付
td = table.findAll("td")[0]
regex = u'<td(.*)>(.*?)</td>'
regdate = re.search(regex, unicode(td)).group(2)
regdate = regdate.replace(u'年', '-') 
regdate = regdate.replace(u'月', '-') 
regdate = regdate.replace(u'日', '') 

#当選番号
num = []
for td in table.findAll("td")[1:10]:
        num.append(re.search(regex, unicode(td)).group(2))

numX1 = num[7].replace('(', '').replace(')', '');
numX2 = num[8].replace('(', '').replace(')', '');

print u"回数：" + kuji_id
print u"日付：" + regdate
print u"当選番号１：" + num[0]
print u"当選番号２：" + num[1]
print u"当選番号３：" + num[2]
print u"当選番号４：" + num[3]
print u"当選番号５：" + num[4]
print u"当選番号６：" + num[5]
print u"当選番号７：" + num[6]
print u"ボーナス数字１：" + numX1
print u"ボーナス数字２：" + numX2

