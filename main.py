import argparse
from utils import export_csv, save_to_mongo, search_DB

from scrape import start_scrape
from bs4_scrape import start_soup


def main():
    parser = argparse.ArgumentParser(description="this script will scrape the Zoomit site with selenium")
    
    # needed to start any browsing
    parser.add_argument("-s", "--scrape", help="enter how many pages should scrape 4-10 (it's exclusive)",type=int)
    
    # scrape with BeautifulSoup instead of selenium
    
    parser.add_argument("-b", "--soup", help="enter how many pages should scrape 4-10 (it's exclusive)",type=int)
    
    # save options
    parser.add_argument("-c", "--csv", action="store_true", help="export to CSV")
    parser.add_argument("-m", "--mongo", action="store_true", help="add items to mongo db")
    
    # search the mongDB
    parser.add_argument("-f", "--find",help="enter the name of the product you want to search the data base",type=str)
    
    # print output in terminal
    parser.add_argument("-p", "--print",help="print the output",action="store_true")
    
    
    args = parser.parse_args()
    
    data = []

    if args.scrape:
        data = start_scrape(args.scrape)
    
    if args.soup:
        data = start_soup(args.soup)

    if args.csv:
        export_csv(data)
    
    if args.mongo:
        save_to_mongo(data)
        
    if args.print:
        print(data)
    
    elif args.find:
        phrase = args.find
        print(search_DB(phrase))
    

if __name__ == "__main__":
    main()
