import requests
from bs4 import BeautifulSoup
import lxml


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",

}
response = requests.get(
    url="https://www.amazon.co.uk/Crucial-MX500-CT1000MX500SSD1-NAND-Internal/dp/B078211KBB/ref=sr_1_4?crid=ZOVX5HZW4Y4L&dchild=1&keywords=ssd+1tb&qid=1613378928&sprefix=ssd%2Caps%2C220&sr=8-4",
    headers=headers,
)
amazon_page = response.text

soup = BeautifulSoup(amazon_page, "lxml")

scrape_price = soup.find(name="span", id="priceblock_ourprice")
price = int(scrape_price.getText().split('£')[1].split('.')[0])

print(price)
print(type(price))

if price < 81:
    print("This item is going for a great price!")