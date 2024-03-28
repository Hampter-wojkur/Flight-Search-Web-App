from selenium import webdriver
from selenium.webdriver.common.by import By
import json

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.flightconnections.com/airport-codes")

airport_lists = driver.find_elements(By.CLASS_NAME, "airport-list")

iata_codes = {}

for airport_list in airport_lists:
    airports = airport_list.find_elements(By.TAG_NAME, "li")
    for airport in airports:
        iata_code = airport.find_element(By.CLASS_NAME, "airport-code").text
        city = airport.find_element(By.CLASS_NAME, "airport-city-country").text
        city_formatted = city.split(",")[0]
        print
        if city_formatted in iata_codes:
            iata_codes[city_formatted] = iata_codes.get(city_formatted,'') + 'to delete: ' + iata_code
        else:
            iata_codes[city_formatted] = iata_code


# print(iata_codes)
            
            
file_name = "iata_codes.json"
with open(file_name, 'w') as file:
    json.dump(iata_codes, file, indent=4)