import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 1. Setup the Browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

if driver == None:
    print("Failed to initialize the browser.")
else : print("Browser initialized successfully.")

url = "https://www.ycombinator.com/companies"
driver.get(url)

time.sleep(5)  # Wait for the page to load

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # Wait for new content to load
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Infinite Scroll logic runs first

# 1. Locate all company card elements using the current class
all_cards = driver.find_elements(By.CLASS_NAME, "_company_i9oky_355")

company_links = [card.get_attribute("href") for card in all_cards]

print(f"Collected {len(company_links)} links. Starting deep crawl...")

all_companies = []

for card in all_cards:
    try:
        #Extract Name using the specific span class
        name = card.find_element(By.CLASS_NAME, "_coName_i9oky_470").text

        # Extract Categories (Pills)
        # We look for all spans with the 'pill' class inside this card
        pill_elements = card.find_elements(By.CLASS_NAME, "_pill_i9oky_33")
        categories = [pill.text for pill in pill_elements if pill.text.strip()]
        
        all_companies.append({
            "company_name": name,
            "categories": categories
        })
        print(f"Captured: {name}") 

    except Exception as e:
        continue

# 5. Save the result as a JSON file
with open('yc_top_20.json', 'w', encoding='utf-8') as f:
    json.dump(all_companies, f, indent=4)

