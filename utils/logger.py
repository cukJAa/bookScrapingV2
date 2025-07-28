import logging
import os


os.makedirs("output/logs", exist_ok=True)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("output/logs/scraper.log", mode='a', encoding='utf-8'),
        logging.StreamHandler()  
    ]
)

logger = logging.getLogger(__name__)
