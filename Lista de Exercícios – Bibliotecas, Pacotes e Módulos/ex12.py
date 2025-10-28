# 12. Escreva um programa que importe o pacote beautifulsoup4 e faça a raspagem de dados (web crawling) de uma página HTML.

from bs4 import BeautifulSoup
import requests
url = 'https://www.example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())