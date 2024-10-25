import requests
from bs4 import BeautifulSoup
from logger import Logger
from typing import Optional

class PriceScraper:
    """
    A class to scrape the current price of a product from an e-commerce page.

    Attributes:
        product_url (str): The URL of the product page to scrape.
        headers (dict): The headers to use for the HTTP request.
    """

    def __init__(self, product_url: str):
        """
        Initializes the PriceScraper with the given product URL.

        Args:
            product_url (str): The URL of the product page to scrape.
        """
        self.product_url = product_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        }
    @Logger.log_execution 
    def fetch_current_price(self) -> Optional[float]:
        """
        Scrapes the current price of the product from the product URL.

        Returns:
            Optional[float]: The current price if found, otherwise None.
        """
        try:
            Logger.log_info("Sending request to fetch the product page with SSL verification disabled.")
            # Disabling SSL verification (not recommended for production)
            response = requests.get(self.product_url, headers=self.headers, verify=False)
            
            if response.status_code == 200:
                Logger.log_info("Product page fetched successfully.")
            else:
                Logger.log_warning(f"Received unexpected status code: {response.status_code}")

            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract price component
            price_element = soup.find('div', class_='Nx9bqj CxhGGd')
            if price_element:
                price_text = price_element.text.strip()
                Logger.log_info(f"Raw price text extracted: {price_text}")

                # Clean and extract price
                price = ''.join(filter(str.isdigit, price_text))
                if price:
                    Logger.log_info(f"Current price is {price}")
                    return float(price)
                else:
                    Logger.log_warning("Failed to clean and extract a valid price.")
                    return None
            else:
                Logger.log_error("Price element not found on the page.")
                return None
        except requests.exceptions.SSLError as ssl_err:
            Logger.log_error(f"SSL Error while scraping price: {ssl_err}")
            return None
        except Exception as e:
            Logger.log_error(f"Error while scraping price: {e}")
            return None
