import argparse
from utils import export_csv

from scrape import start_scrape

# from scrape_approach_2 import start_scrape_2 uncomment and replace "start_scrape_2" with "start_scrape" func


def main():
    parser = argparse.ArgumentParser(description="this script will scrape the zoomit site with selenium")
    parser.add_argument("page_number", help="enter howmany pages should scrape 4-10 (it's exclusive)")
    parser.add_argument("--csv", action="store_true", help="export to CSV")

    args = parser.parse_args()

    res = start_scrape(args.page_number)

    if args.csv:
        export_csv(res)

    else:
        print(res)


if __name__ == "__main__":
    main()
