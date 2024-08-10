from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def set_up_driver():
    #"""Set up Chrome WebDriver and return the driver instance."""
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def search_term(driver, search_engine_url, search_query):
    """Perform a search operation on the specified search engine."""
    logging.info(f"Navigating to {search_engine_url}")
    driver.get(search_engine_url)
    
    logging.info(f"Searching for the term: {search_query}")
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

def verify_results(driver):
    """Verify that search results are displayed."""
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3"))
        )
        logging.info("Search results are present.")
        return True
    except:
        logging.error("No search results found.")
        return False

def main():
    driver = set_up_driver()
    try:
        search_engine_url = "https://www.google.com"
        search_query = "Test Automation"
        
        search_term(driver, search_engine_url, search_query)
        
        if verify_results(driver):
            logging.info("Test Passed.")
        else:
            logging.error("Test Failed.")
    finally:
        logging.info("Browser is closing")
        driver.quit()

if __name__ == "__main__":
    main()
