from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

# this approach is **discontinued** :)))))))))) dont use this

def start_scrape_2(page_num):
    data = []
    choice = ""

    choice_list = ["mobile", "laptop", "tablet", "wearables", "tv"]

    while choice not in choice_list or choice == "help":
        choice = str(input('type your target category or type "help" to see categories : ')).lower()
        if choice == "help":
            print(f"\nCategories are : {choice_list} \n")
        elif choice in choice_list:
            break
        else:
            print("empty or wrong -> using default [mobile]")
            choice = "mobile"
            break

    driver = webdriver.Chrome()
    driver.get(f"https://www.zoomit.ir/product/list/{choice}/")  # difference between scrape 1 and 2

    for i in range(1, int(page_num)):
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

        next_page_button = driver.find_element(
            By.XPATH,
            f"/html/body/div[2]/div[7]/div[3]/div[2]/div[1]/nav/ul/li[{str(i)}]/a",  # difference between scrape 1 and 2
        )
        next_page_button.click()
        sleep(5)

    driver.quit()

    return data
