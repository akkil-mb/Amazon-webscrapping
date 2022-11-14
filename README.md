# Amazon-webscrapping
import datetime
import time

import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import csv
import smtplib


url = 'https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5XSG8Z/ref=sr_1_3?crid=2AX3EVCC389MJ&keywords=macbook+air&qid=1665925608&qu=eyJxc2MiOiIzLjg0IiwicXNhIjoiMi45NCIsInFzcCI6IjIuNjEifQ%3D%3D&sprefix=macbook+a%2Caps%2C445&sr=8-3'
header = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15'
# user agenet identifier : https://httpbin.org/get

page = requests.get(url, header)
soup1 = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

header = ['Title', 'Price', 'Date']
with open('Amazon_web_scrapping_m1.csv', 'w', newline='', encoding = 'UTF8') as f:
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
    with open('Amazon_web_scrapping_m1.csv', 'a+', newline='', encoding = 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

while (True):
    check_price()
    time.sleep(5)

df = pd.read_csv(r'/Users/akkil/Desktop/Python_programs/Projects/Final Projects/Amazon_web_scrapping.csv')
print(df)



