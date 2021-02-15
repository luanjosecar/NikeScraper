from bs4 import BeautifulSoup
import requests
from objects import Product

def NikeScraper():
    
    page = requests.get("https://www.nike.com.br/Snkrs/#estoque")
    soup = BeautifulSoup(page.content, 'html.parser')

    producDiv = soup.find_all('div', class_='produto__imagem')

    list = []

    for img in producDiv:
        imgSrc = img.find('img')

        imgTag = imgSrc.get('data-src')
        productName = imgSrc.attrs['alt']

        productId = productName[-12:]
        productName = productName[:-19]

        productBuyDiv = img.find(class_='produto__hover')
        productBuy = productBuyDiv.find('a')

        list.append(Product(productName, imgTag, productBuy.attrs['href'], productId))

    return list