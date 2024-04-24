import os,time,io,sys,csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stdin = io.TextIOWrapper(sys.stdin.detach(),encoding="utf-8")

service = Service(executable_path='./chromedriver.exe')
driver = webdriver.Chrome(service=service)

arr = []

for i in range(1,3):
    base_url = f'https://yozm.wishket.com/magazine/list/plan/?page={i}&sort=&q='
    print(base_url)

    driver.get(base_url)

    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #list 형태로 tmp에 담김
    tmp = soup.select("body > div.layout > div > div.list-cover > div:nth-child(1) > div > div.flex-box.list-item-box > div.item-main.text900 > a.item-title.link-text.link-underline.text900")
    # print(tmp[0].get('href'))
        
    tmp2 = soup.find_all("a",class_ = "item-title link-text link-underline text900")


    # 링크를 담아두는 리스트 
    
    for tt in tmp2:
        arr.append("https://yozm.wishket.com"+tt.get("href"))
    
print(arr)

for link in arr:
    driver.get(link)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    content = soup.find("div",class_="next-news-contents news-highlight-box")
    print(content)
    exit()
    

