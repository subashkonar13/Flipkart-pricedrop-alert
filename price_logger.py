import csv
from datetime import datetime
import logging
from typing import Optional

class PriceLogger:
    """
    A class to log the product price to a CSV file and retrieve the last logged price.

    Attributes:
        price_history_file (str): The path to the CSV file for logging the price history.
    """

    def __init__(self, price_history_file: str):
        """
        Initializes the PriceLogger with the given CSV file.

        Args:
            price_history_file (str): The path to the CSV file for logging the price history.
        """
        self.price_history_file = price_history_file

    def log_price(self, price: float) -> None:
        """
        Logs the given price to the CSV file with a timestamp.

        Args:
            price (float): The price to log.
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            with open(self.price_history_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, price])
            logging.info(f"Logged new price: ${price}")
        except Exception as e:
            logging.error(f"Error logging price: {e}")

    def get_last_logged_price(self) -> Optional[float]:
        """
        Retrieves the last logged price from the CSV file.

        Returns:
            Optional[float]: The last logged price if available, otherwise None.
        """
        try:
            with open(self.price_history_file, 'r') as file:
                last_line = list(csv.reader(file))[-1]
                return float(last_line[1])
        except (FileNotFoundError, IndexError):
            logging.warning("Price history file is not found or empty.")
            return None
