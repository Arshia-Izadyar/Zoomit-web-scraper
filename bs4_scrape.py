from bs4 import BeautifulSoup
import requests
from requests.exceptions import Timeout, TooManyRedirects, ReadTimeout
from datetime import datetime

def start_soup(page_num):
    data = []
    base = "https://www.zoomit.ir"
    choice = ""

    choice_list = ["mobile", "laptop", "tablet", "wearables", "tv", "cpu", "vga"]  # all browsable products

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
        
    start_time = datetime.now()
    for i in range(1, page_num+1):
        try:
            print(f"scraping page : {i}")
            res = requests.get(f"{base}/product/list/{choice}/page/{str(i)}/")
            res.raise_for_status()
            soup = BeautifulSoup(res.text, "html.parser")
            products = soup.find_all("div", attrs={"class": "productSummery"})
            for prod in products:
                title = prod.find("span", class_="productEnglishTitle").text
                price = prod.find("div", class_="productSummery__prices--highlited").text.split(" ")[0]
                rate = prod.find("span", class_="productSummery__rate").text
                link = prod.find("a", class_="button")
                if not link.get("href").startswith(base):
                    link = base + link.get("href")            
                data.append(
                    {
                    "title": title,
                    "rate": rate,
                    "price": price,
                    "link": link.get("href"),
                    "created_date": datetime.now()
                    }
                )
            
        except (Timeout, TooManyRedirects, ReadTimeout) as e:
            print("Error occurred :\t", e)
    
    print("Crawling time : {}".format(datetime.now() - start_time))

    print("Scraping ended !!")
    return data
            
            
        
        
        
        
if __name__ == "__main__":
    start_scrape(1)