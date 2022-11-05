import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url="https://www.psychologytoday.com/us/therapists/california?sid=6268171cd22b4&page=200"
page=requests.get(url)
print(page.status_code)

soup=BeautifulSoup(page.content,'html.parser')
link=soup.find(class_='results')
##link1=link.find('a')
print (link)
##last_links=soup.find(class_='AlphaNav')
##last_links.decompose()
##i=0
##for names1 in (zcontent1):
##    names=names1.contents[0]
##    links='https://web.archive.org'+names1.get('href')
##    print(names)
##    print(links)
