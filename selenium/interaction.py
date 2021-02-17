from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/usr/bin/brave"
chrome_driver_path = "/home/sk/selenium-webdriver/chromedriver"
driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)
driver.get("https://secure-retreat-92358.herokuapp.com/")


# wiki_entries = driver.find_element_by_xpath('//*[@id="main_page_mp-mp"]/tbody/tr[1]/td/table/tbody/tr[1]/td[1]/p/b/a')
# wiki_entries.click()
# all_portals = driver.find_element_by_link_text("All portals")
#all_portals.click()

first_name = driver.find_element_by_name("fName")
first_name.send_keys("sbkj")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("isjsbkj")
email = driver.find_element_by_name("email")
email.send_keys("sbjk@yahoo.co")

button = driver.find_element_by_tag_name("button")
button.click()

#driver.quit()