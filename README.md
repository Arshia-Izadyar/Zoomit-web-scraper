# selenium-web-scraper

A web scraper with selenium-python for <a href="https://www.zoomit.ir">Zoomit.ir</a> site

with support for **_CSV_** output and saving files to **Data-Base**

you can scrape products in many categories like:

"mobile", "laptop", "tablet", "wearables", "tv", "cpu", "vga"

## How to use?

1.  First install requirements

        pip install -r requirements.txt

2.  install the <a href="https://sites.google.com/chromium.org/driver/">Chrome Driver</a> for selenium
3.  run the script using arguments (will list arguments below)

        python main.py --print --scrape 5
    
6. after running the script you have to type the target category in the input field like **vga** or **cpu** the **default is mobile** category

### Arguments 
#### --scrape / -s
Use -s or --scrape and the give the number of pages you want to sceape default

    python main.py --scrape 5
        
****this command is necessary to start the webscraping function***

#### --print / -p
use --print or -p after using --scrape to print the data in terminal

    python main.py -s 3 --print

### --mongo / -m
this ard will save the scraped data to ***__MongoDB__*** 

    python main.py -s 3 --mongo

### --find / -f 
this will search database with the value you set next to it (icontain)

    python main.py --find Apple

### --csv / -c 

this arg will create a csv file with scraped data

    python main.py -s 3 --csv


## Notes
1. you can change the scraper file to scrape_approach_2.py its has a small difference in the code and might skipe some products

2. utils.py contains function for creating a csv file / adding files to DB / run a query in DB

![image](https://github.com/Arshia-Izadyar/selenium-web-scraper/assets/110552657/0a73e409-8db1-41b2-bbb2-1bea04a1bf70)


