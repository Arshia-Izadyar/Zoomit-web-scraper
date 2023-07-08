from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException

from datetime import datetime


def start_scrape(page_num):
    
    data = []
    choice = ""

    choice_list = ["mobile", "laptop", "tablet", "wearables", "tv", "cpu", "vga"]

    while choice not in choice_list or choice == "help":
        choice = str(input('type your target category or type "help" to see categories : ')).lower()
        if choice == "help":
            print(f"\n Categories are : {choice_list} \n")
        elif choice in choice_list:
            break
        else:
            print("empty or wrong -> using default [mobile]")
            choice = "mobile"
            break

    driver = webdriver.Chrome()
    driver.headless = True
    print('started scraping ... ')
    
    start_time = datetime.now()

    for i in range(1, int(page_num) + 1):
        driver.get(f"https://www.zoomit.ir/product/list/{choice}/page/{str(i)}/") # difference between scrape 1 and 2

        try:
            prods = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "productSummery"))
            )

        except Exception as e:
            raise e

        for prod in prods:
            try:
                title = prod.find_element(By.CLASS_NAME, "productEnglishTitle")

                rate = prod.find_element(By.CLASS_NAME, "productSummery__rate")

                price = prod.find_element(
                    By.CSS_SELECTOR,
                    ".productsList .c-productsList__inLine .productSummery .productSummery__prices > div.productSummery__prices--highlited span",
                )

                data.append({"title": title.text, "rate": rate.text, "price": price.text})

            except NoSuchElementException:
                continue

    driver.quit()
    print('Crawling time : {}' .format(datetime.now() - start_time))
    print('successfuly Finished')

    return data
