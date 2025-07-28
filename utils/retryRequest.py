import requests
import time
from utils.logger import logger

def safe_get(session, url, retries=3, delay=2, timeout=5):
    for attempt in range(1, retries + 1):
        try:
            response = session.get(url, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logger.warning(f"Attempt {attempt} failed for {url}: {e}")
            time.sleep(delay)
    logger.error(f"All {retries} attempts failed for {url}")
    return None