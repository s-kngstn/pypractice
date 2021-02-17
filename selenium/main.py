from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/usr/bin/brave"
chrome_driver_path = "/home/sk/selenium-webdriver/chromedriver"
driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)

# driver.get("https://www.amazon.co.uk/Crucial-MX500-CT1000MX500SSD1-NAND-Internal/dp/B078211KBB/ref=sr_1_4?crid=ZOVX5HZW4Y4L&dchild=1&keywords=ssd+1tb&qid=1613378928&sprefix=ssd%2Caps%2C220&sr=8-4")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

driver.get("https://www.python.org")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_list = driver.find_elements_by_css_selector(".medium-widget.event-widget.last div.shrubbery ul.menu li")
upcoming_events = {}
li_num = 1
dict_num = 0
for events in range(0, len(event_list)):
    date = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{li_num}]/time')
    event = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{li_num}]/a')
    li_num += 1
    upcoming_events[dict_num] = {
        "time": date.text,
        "name": event.text,
    }
    dict_num += 1
print(upcoming_events)

# driver.close() #<-- will close the active tab
driver.quit() #<-- will quit browser
