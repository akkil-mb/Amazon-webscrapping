import datetime
import time

import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import csv
import smtplib


url = 'https://www.amazon.in/Apple-iPhone-128GB-Product-RED/dp/B0BDJH3V3Q/ref=sr_1_5?crid=1426CVZX04BHX&keywords=iphone%2B13&qid=1665918991&qu=eyJxc2MiOiI0LjU4IiwicXNhIjoiNC4wNCIsInFzcCI6IjMuNDQifQ%3D%3D&sprefix=iphone%2Caps%2C770&sr=8-5&th=1'
header = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15'
# user agenet identifier : https://httpbin.org/get

page = requests.get(url, header)
soup1 = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

header = ['Title', 'Price', 'Date']
with open('Amazon_web_scrapping.csv', 'w', newline='', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)


def check_price():
    title = soup2.find(id='productTitle').get_text()
    t_title = title.strip()
    price = soup2.find(class_ = "a-offscreen").get_text()
    p_price = price.strip()[1:]
    print(t_title)
    print(p_price)

    time = datetime.now()
    print(time)

    data = [t_title, p_price, time]
    with open('Amazon_web_scrapping.csv', 'a+', newline='', encoding = 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

while (True):
    check_price()
    time.sleep(5)

df = pd.read_csv(r'/Users/akkil/Desktop/Python_programs/Projects/Final Projects/Amazon_web_scrapping.csv')
print(df)



