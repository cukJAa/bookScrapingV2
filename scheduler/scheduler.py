import schedule
import time
from scraper.webScraper import scrape_books
import logging

logging.basicConfig(level=logging.INFO)

def startScheduler():
    logging.info("Starting the initial scrape...")
    scrape_books()
    logging.info("Scheduling the scraping task every  5 minutes...")
    
    schedule.every(5).minutes.do(scrape_books)

    while True:
        schedule.run_pending()
        time.sleep(1)
        