# selenium-web-scraper
A web scraper with selenium-python for <a href="https://www.zoomit.ir">Zoomit.ir</a> site

you can scrape products in many categories like:

"mobile", "laptop", "tablet", "wearables", "tv", "cpu", "vga"

## How to use?

1) First install requirements

       pip install -r requirements.txt


 2) install the <a href="https://sites.google.com/chromium.org/driver/">Chrome Driver</a> for selenium
 3) run the Chrome Driver
 4) open terminal and run the script

        python main.py {number of pages that you want to scrape like 5 } --csv
    exp:
    
        python main.py 5 --csv

  6) after running the script you have to type the target category like vga or cpu the default is mobile category

## Notes

1) adding ***--csv*** will generate a csv file for the results: 

![image](https://github.com/Arshia-Izadyar/selenium-web-scraper/assets/110552657/0a73e409-8db1-41b2-bbb2-1bea04a1bf70)




2) you can change the scraper file to scrape_approach_2.py its has a small difference in the code and might skipe some products

3) utils.py contain a function for creating a csv file


    
