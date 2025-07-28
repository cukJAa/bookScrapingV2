from bs4 import BeautifulSoup
import re
import requests
import pandas as pd
from datetime import datetime 
from utils.logger import logger
from utils.retryRequest import safe_get


def imageToList(soup):
    image = soup.find_all("img")
    imageList =[]
    for img in image:
        imageSource = img['src']
        imageSource = imageSource.replace("../", "https://books.toscrape.com/")
        imageList.append(imageSource)
    return imageList

def starToList(url):
    stars = url.find_all("p", class_ = "star-rating")
    starRating = []
    for star in stars:
        star_map = {
            "One": f"{1} out of {5}",
            "Two": f"{2} out of {5}",
            "Three": f"{3} out of {5}",
            "Four": f"{4} out of {5}",
            "Five": f"{5} out of {5}"
        }
        starRating.append(star_map.get(star["class"][1], "0 out of 5"))
        
    return starRating

def titlesToList(url):
    titles = url.find_all("h3")
    bookTitles = []
    for t in titles:
        title = t.a["title"]
        bookTitles.append(title)
    return bookTitles


def pricestoList(url):
    prices = url.find_all(string=re.compile("£"))
    cleaned_prices = []
    for price in prices:
        clean_price = price[1:]
        cleaned_prices.append(clean_price)
    return cleaned_prices


all_books = []
def scrape_books():
    currentTime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with pd.ExcelWriter(f"output/booksFromPagesV2[{currentTime}].xlsx", engine="openpyxl", mode='w') as writer:
        logger.info(f"Scraping started at [{currentTime}] ")
        for i in range(1, 51):
            logger.info(f"Scraping page {i}")
            session = requests.Session()
            url = f"https://books.toscrape.com/catalogue/page-{i}.html"
            result = safe_get(session, url)
            result.encoding = "utf-8"

            if result is None:
                logger.error(f"Skipping page {i} due to faile request")
                continue

            soup = BeautifulSoup(result.text, "html.parser")

            
            books = [list(book_tuple) for book_tuple in zip(imageToList(soup), starToList(soup), titlesToList(soup), pricestoList(soup))]
            
            df = pd.DataFrame(books, columns=["Image", "Rating", "Title", "Price"])
            df.to_excel(writer, index=False, sheet_name=f"Books Page {i}" )
            
            all_books.extend(books)
            print(f"Page {i} scraped and saved to CSV and EXCEL")

    df_all = pd.DataFrame(all_books, columns=[  "Image", "Rating", "Title", "Price"])
    df_all.to_csv(f"output/booksFromPagesV2[{currentTime}].csv", index=False) 
    currentTimeAfterScrape = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    logger.info(f"All pages scraped saved to CSV and EXCEL at [{currentTimeAfterScrape}]")

