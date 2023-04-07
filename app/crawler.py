import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

def startCrawler():
    url='https://land.bizmk.kr/memul/list.php?bubcode=4150025300&mgroup=H&mclass=&bdiv=A&areadiv=&aptcode=&mseq=&xpos=127.50590456797231&ypos=37.265623765733665&JMJ='
    # 마법의 명령어
    soup=bs(ur.urlopen(url).read(),'html.parser')

    rlt = ""
    # for i in soup.find_all('tr',{"class":"TRBGColor"}):
    for i in soup.find_all('tbody'):
        rlt += i.text
    rlt = re.sub('\t','',rlt)
    rlt = re.sub('\r','',rlt)
    rlt = re.sub(',','',rlt)

    # rlt = """
    #
    # """

    result = []
    for line in rlt.split("\n"):
        word_result = []
        for word in line.split(" "):
            if word == '매매' or word == '전세' or word == '월세' or word == '단기임대':
                word_result.append('\n')
            if word != '':
                word_result.append(word)
        if len(word_result) :
            result.append(" ".join(word_result))

    return(" ".join(result))
