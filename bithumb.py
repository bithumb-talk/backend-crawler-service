import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.bithumb.com/'
req_header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
res = requests.get(url, headers=req_header)

if res.ok:
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    coins = soup.select('#sise_list > tbody > tr')

    with open('bithumb.csv','w',encoding='utf-8') as f:
        for coin in coins:
            names = coin.select('td:nth-child(1) > div > p > a > strong')
            symbols = coin.select('td:nth-child(1) > div > p > a > span')
            for name_obj, symbol_obj in zip(names,symbols):
                name = re.sub('신규 공시', '', name_obj.text.strip())
                symbol = symbol_obj.text.strip().replace('/','_')
                if symbol.endswith('KRW'):
                    f.write(f'{name},{symbol}\n')
