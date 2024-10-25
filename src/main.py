from price_scraper import PriceScraper
from price_logger import PriceLogger
from email_notifier import EmailNotifier
from scheduler import Scheduler
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class PriceTracker:
    """
    A class that orchestrates the entire price tracking workflow.

    Attributes:
        scraper (PriceScraper): The scraper used to fetch the current price.
        logger (PriceLogger): The logger used to record price history.
        notifier (EmailNotifier): The notifier used to send email alerts.
    """

    def __init__(self, scraper: PriceScraper, logger: PriceLogger, notifier: EmailNotifier):
        """
        Initializes the PriceTracker with a scraper, logger, and notifier.

        Args:
            scraper (PriceScraper): The scraper used to fetch the current price.
            logger (PriceLogger): The logger used to record price history.
            notifier (EmailNotifier): The notifier used to send email alerts.
        """
        self.scraper = scraper
        self.logger = logger
        self.notifier = notifier

    def track_price(self) -> None:
        """
        Checks the current product price and compares it with the last logged price.
        If the current price is lower, it logs the new price and sends an email notification.
        """
        try:
            current_price = self.scraper.fetch_current_price()
            if current_price is not None:
                last_logged_price = self.logger.get_last_logged_price()
                
                # Send email only if current price is less than the last logged price
                if last_logged_price is None or current_price < last_logged_price:
                    self.logger.log_price(current_price)
                    self.notifier.send_price_alert(current_price, self.scraper.product_url)
                    logging.info(f"Price drop detected! New price: ${current_price}")
                else:
                    logging.info(f"No price drop. Current price: ${current_price}, Last logged price: ${last_logged_price}")
            else:
                logging.warning("Failed to retrieve the current price.")
        except Exception as e:
            logging.error(f"Error in price tracking: {e}")


if __name__ == "__main__":
    # Configuration settings
    product_url = 'https://www.flipkart.com/...'  # Replace with the actual product URL
    price_history_file = 'price_history.csv'
    sender_email = 'your_email@example.com'
    receiver_email = 'receiver_email@example.com'
    email_password = 'your_password'  # Note: For real applications, securely handle passwords

    # Initialize components
    scraper = PriceScraper(product_url)
    logger = PriceLogger(price_history_file)
    notifier = EmailNotifier(sender_email, email_password, receiver_email)
    tracker = PriceTracker(scraper, logger, notifier)

    # Schedule the price tracking every hour
    scheduler = Scheduler()
    scheduler.schedule_task(tracker.track_price, interval_hours=1)
    
    # Start the scheduler
    logging.info("Starting price tracking scheduler.")
    scheduler.run()
