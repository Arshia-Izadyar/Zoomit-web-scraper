import argparse
from utils import export_csv, save_to_mongo

from scrape import start_scrape

# from scrape_approach_2 import start_scrape_2 # uncomment and replace "start_scrape_2" with "start_scrape" func


def main():
    parser = argparse.ArgumentParser(description="this script will scrape the Zoomit site with selenium")
    parser.add_argument("page_number", help="enter how many pages should scrape 4-10 (it's exclusive)")
    parser.add_argument("--csv", action="store_true", help="export to CSV")
    parser.add_argument("--mongo", action="store_true", help="add items to mongo db")
    args = parser.parse_args()

    data = start_scrape(args.page_number)

    if args.csv:
        export_csv(data)
    
    if args.mongo:
        save_to_mongo(data)
        

    else:
        print(data)


if __name__ == "__main__":
    main()
