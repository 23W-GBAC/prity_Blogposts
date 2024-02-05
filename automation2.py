from xml import etree
import requests
from bs4 import BeautifulSoup
from urllib3.util import url

URL = 'https://www.ebay.com/itm/144343762061?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D259940%26meid%3D9cbd7cf734444fe6a4b020f3d74a3208%26pid%3D101875%26rk%3D1%26rkt%3D4%26sd%3D235414588565%26itm%3D144343762061%26pmt%3D1%26noa%3D1%26pg%3D4429486%26algv%3DSimplAMLv11WebTrimmedWithMfgPhase2WithCassiniVisualRankerAndBertRecallWithPLXSizeFilterCPCAuto%26brand%3DMichael%2BKors&_trksid=p4429486.c101875.m1851&amdata=cksum%3A1443437620619cbd7cf734444fe6a4b020f3d74a3208%7Cenc%3AAQAIAAABIBx0leWtGLIhPbwRGZh8DcKRUFunbptXdFZPDYlc%252Fr57W3HJiiVhrIP3uBWisH7Xh%252FIKKr2KW763RkYVMSCIRVXCOdpijsX7QSHVjp83EbPP7W%252BrFTihPHt4cDbYUoYUKE47xNEhNqrQ9N%252B7U8PgjPziIG4vsfH1noVy4X%252Buf849dejuzbIudc1ZNgkWg7Lixp7r6I%252F8u1yrVsJTNJNds6pHkLm552p%252BBHBhCpXqz4IHQ%252B64fmWNaG2RZntLvMFKPmgkSbLkf6NWXju7ElLM7c2DnjCJZ8bTD0J0wM%252BaQWtt6Z8f0tBLhBU8Y%252B36n84YrU%252FYuYN9yOShvzPf5dxbLjEeVOay8kEB6iTSE%252BDiYsIxWxh1zU8p2dMXIHHMsQEJYg%253D%253D%7Campid%3APLP_CLK%7Cclp%3A4429486&epid=8051555507'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

product_title = soup.find(class_='ux-textspans ux-textspans--BOLD').get_text()
print(product_title)

product_price = soup.select('#mainContent > div > div.vim.x-price-section.mar-t-20 > div > div > div > span')

for p in product_price:
    print(p.text)
    product_price_value = int(p.text[4:7])
    print(product_price_value)

def check_price():
    if (product_price_value < 400):
        print('Congrats! The price has fallen to : $' , product_price_value)
    else:
        print('Sorry, The price is still $400')

if __name__ == '__main__':
    check_price()
