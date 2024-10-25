import csv
import os
from datetime import datetime
from logger import Logger
from typing import Optional

class PriceLogger:
    """
    A class to log the product price to a CSV file and retrieve the last logged price.

    Attributes:
        price_history_file (str): The path to the CSV file for logging the price history.
    """

    def __init__(self, price_history_file: str):
        """
        Initializes the PriceLogger with the given CSV file. Creates the file with headers if it doesn't exist.

        Args:
            price_history_file (str): The path to the CSV file for logging the price history.
        """
        self.price_history_file = price_history_file
        # Ensure the file exists with headers on initialization
        self._initialize_file()
        
    @Logger.log_execution 
    def _initialize_file(self) -> None:
        """
        Checks if the CSV file exists. If not, creates it with headers.
        """
        if not os.path.exists(self.price_history_file):
            try:
                with open(self.price_history_file, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Timestamp', 'Price'])  # Headers for the CSV file
                Logger.log_info(f"Created price history file with headers at: {self.price_history_file}")
            except Exception as e:
                Logger.log_error(f"Error creating price history file: {e}")
                
    @Logger.log_execution 
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
            Logger.log_info(f"Logged new price: ${price}")
        except Exception as e:
            Logger.log_error(f"Error logging price: {e}")
            
    @Logger.log_execution
    def get_last_logged_price(self) -> Optional[float]:
        """
        Retrieves the last logged price from the CSV file.

        Returns:
            Optional[float]: The last logged price if available, otherwise None.
        """
        try:
            with open(self.price_history_file, 'r') as file:
                reader = csv.reader(file)
                last_lines = list(reader)

                # Check if the file has at least one valid entry
                if not last_lines or len(last_lines) < 2:
                    Logger.log_warning("Price history file is empty or does not contain price entries.")
                    return None
                
                # Get the last entry (not the header)
                last_price_entry = last_lines[-1]

                # Attempt to convert to float, ignore any invalid formats
                try:
                    price = float(last_price_entry[1])
                    return price
                except ValueError:
                    Logger.log_warning(f"Invalid price format found: {last_price_entry[1]}")
                    return None
                
        except FileNotFoundError:
            Logger.log_warning("Price history file not found.")
            return None
        except Exception as e:
            Logger.log_error(f"Unexpected error: {e}")
            return None
