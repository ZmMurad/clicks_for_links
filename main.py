import requests
from settings import *
from pprint import pprint
from urllib.parse import urlparse


user_url=urlparse(input())
host="https://api-ssl.bitly.com/v4/"





def shorten_link(token,long_url):
    url=f"{host}bitlinks"
    json={"long_url":long_url}
    response=requests.post(url,json = json, headers=token)
    response.raise_for_status()
    bitlink=response.json()["link"]
    return bitlink

def count_clicks (token,link):
    link=urlparse(link)
    link=f"{link.netloc}{link.path}"
    url=f"{host}bitlinks/{link}/clicks/summary"
    respone=requests.get(url,headers=token)
    respone.raise_for_status()
    return respone.text


# try:
#     print('Битлинк',shorten_link(TOKEN, data) )
# except Exception as error:
#     print(f"Вы получили ошибку - {error}")

def is_bitlink(url):
    if url.netloc=="bit.ly":
        return True
    return False

if is_bitlink(user_url):
    try:
        print('Битлинк количество',count_clicks (TOKEN, user_url.geturl()))
    except Exception as error:
        print(f"Вы получили ошибку - {error}")
else:
    try:
        print('Битлинк',shorten_link(TOKEN, user_url.geturl()) )
    except Exception as error:
        print(f"Вы получили ошибку - {error}")
