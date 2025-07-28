Book scraper with scheduler / Basic automation pipeline

This Python project scrapes book data from a website every 5 minutes using a scheduler. It saves the results into CSV files and XLSX files where each page is a worksheet, and logs all actions for reliability and debugging.

Folder Structure

project/
├── scraper/ # Contains the scraping logic (webScraper.py)
├── scheduler/ # Runs the scheduled scraping every 5 mins (scheduler.py)
├── output/ # Where logs and scraped data are stored
├── utils/ # Contains logging and retry logic
├── main.py # Starts the whole program
├── requirements.txt
└── README.md


How it works 

'main.py'  - starts the program 
It runs 'scheduler.py' from the 'scheduler' folder.
The scheduler uses 'scheduler.py' to run the 'webScraper' from 'scraper' folder every 5 minutes using 'schedule'
The scraper user 'requests', 'BeautifulSoup4' and 'retryRequests' to fetch books data from https://books.toscrape.com
Data is saved in 'output/' folder, and logs are written to 'output/logs/scraper.log'


How to run 

Clone repository 
Install requrements (pip install -r requirements.txt)
Run the program (python main.py)


List of main libraries used:

requests
beautifulsoup4
schedule
pandas
logging

Output

ouput/booksFromPagesV2[datetime].csv -> contains book data with named columns at index 0 (ImageUrl, Rating, Title, Price)
ouput/booksFromPagesV2[datetime].xlsx -> contains book data with named columns at index 0 (ImageUrl, Rating, Title, Price) 
                                         with pagination each page of URL into worksheet named Book Page (the number of page) 
ouput/logs/scraper.log -> contains full log history  
Every scheduled run give a new file .csv and .xlsx with the timestamp of the time scraped