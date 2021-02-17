import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

ZILLOW_WEB_ADDR = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",

}

response = requests.get(url=ZILLOW_WEB_ADDR, headers=headers)
zillow_web = response.text
soup = BeautifulSoup(zillow_web, "html.parser")

prices = soup.find_all(name="div", class_="list-card-price")
price_list = [price_tag.getText() for price_tag in prices]

links = soup.find_all(name="a", class_="list-card-link list-card-img")
links_list = [link_tag.get("href") for link_tag in links]

address = soup.find_all(name="address", class_="list-card-addr")
addr_list = [addr_tag.getText() for addr_tag in address]

# print(len(price_list))
# print(len(addr_list))
# print(len(links_list))

SF_RENTING_FORM = "https://docs.google.com/forms/d/e/1FAIpQLScOqlvd-fee6ebH1m8HST80HwNR7y-Q-sWZhkymCyLp_kbgZw/viewform?usp=sf_link"

options = Options()
options.binary_location = "/usr/bin/brave"
chrome_driver_path = "/home/sk/selenium-webdriver/chromedriver"
driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)

num = 0
for _ in range(0, len(links_list)):
    driver.get(SF_RENTING_FORM)
    address_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add_address = address_input.send_keys(f"{addr_list[num]}")

    price_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add_price = price_input.send_keys(f"{price_list[num]}")

    link_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add_link = link_input.send_keys(f"https://www.zillow.com{links_list[num]}")

    button = driver.find_element_by_class_name("exportButtonContent")
    button.click()
    num += 1