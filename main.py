google_forms_link="https://docs.google.com/forms/d/e/1FAIpQLScLTMBqdtBHSN1UJUdx77sha6lu6WSncmajRqePPJbL1f5N9Q/viewform?usp=sf_link"
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome()
import time
from bs4 import BeautifulSoup
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
"Accept-Language":"en-US,en;q=0.9"
}
response = requests.get(
    "https://www.nobroker.in/property/rent/hyderabad/Gachibowli/?searchParam=W3sibGF0IjoxNy40NDAwODAyLCJsb24iOjc4LjM0ODkxNjgsInBsYWNlSWQiOiJDaElKMzg3ZWRxS1R5enNSNGtTVGI1N25FaXciLCJwbGFjZU5hbWUiOiJHYWNoaWJvd2xpIiwic2hvd01hcCI6ZmFsc2V9XQ==&sharedAccomodation=0&buildingType=AP&isMetro=false&radius=2.0&type=BHK1,BHK2&rent=0,25000&availability=within_15_days&furnishing=FULLY_FURNISHED,SEMI_FURNISHED&parking=TWO_WHEELER,FOUR_WHEELER",
    headers=headers)
rents_data=response.text

soup=BeautifulSoup(rents_data,"html.parser")

all_link_elements = soup.select(".heading-6  a")
all_links=[]
prices=[]
all_addresses=[]
for link in all_link_elements:
    address=link.getText()
    all_addresses.append(address)
    href = link["href"]
    price=href.split("/")[2].split("-")[-1]
    prices.append(price)

    if "http" not in href:
        all_links.append(f"https://www.nobroker.in{href}")
    else:
        all_links.append(href)
print(all_addresses)
print(prices)
print(all_links)

for n in range(5):
    driver.get(google_forms_link)
    time.sleep(2)
    address_name=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_name.send_keys(all_addresses[n])
    price_month = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_month.send_keys(prices[n])

    property_link = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link.send_keys(all_links[n])

    submit=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()

