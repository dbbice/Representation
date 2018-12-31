import requests
import bs4
from bs4 import BeautifulSoup
import traceback
from xlwt import *
import re
import csv

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def getPeopleList(html):
	soup = BeautifulSoup(html, 'html.parser')
	div= soup.findAll('div', attrs={'class': 'listItem'})
	# print(div)
	for ali in div:
		try:
			plst=[]
			m = ['','','','']
			if isinstance(ali, bs4.element.Tag):
				a=ali.find('a')
				# print(a.text)
				href=a.attrs['href']
				m[0]=a.text
				
				zhicheng=ali.find('div',attrs={'class':'level'})
				m[1]=zhicheng.text
				
				danwei=ali.find('p',attrs={'class':'dw'})
				aa=danwei.find('a')
				m[2]=aa.text
				
				# print(m[0])
				# print(m[1])
				# print(m[2])
				
			
			peohtml = getHTMLText(href)
			soup = BeautifulSoup(peohtml, 'html.parser')
			div= soup.find('div', attrs={'id': 'introText'})
			pptext=div.find('p')
			m[3]=pptext.text
			# for pi in pptext:
			# 	m[3].append(pi.text)
			
			for i in range(len(m)):
				plst.append(m[i])
			print(plst)
			write_data(plst,'H:\jtdoctor.csv')

			# lst.append(plst)
		except:
			# traceback.print_exc()
			continue



def write_data(data, name):
    file_name = name
    with open(file_name, 'a', errors='ignore', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows([data])
 


def main():
    # abc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(938,7109):
	    # url = 'http://www.mingyihui.net/top_doctorlist_1.html'+str(i)
	    print(i)
	    url = 'https://ysk.familydoctor.com.cn/area_0_0_0_0_0_'+str(i)+'.html'
	    html = getHTMLText(url)
	    # print(html)
	    getPeopleList(html)
	    

main()