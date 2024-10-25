from price_scraper import PriceScraper
from price_logger import PriceLogger
from email_notifier import EmailNotifier
from scheduler import Scheduler
from logger import Logger


# Configure logging
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PriceTracker:
    """
    A class that orchestrates the entire price tracking workflow.

    Attributes:
        scraper (PriceScraper): The scraper used to fetch the current price.
        logger (PriceLogger): The logger used to record price history.
        notifier (EmailNotifier): The notifier used to send price drop emails.
    """

    def __init__(self, scraper: PriceScraper, logger: PriceLogger, notifier: EmailNotifier):
        """
        Initializes the PriceTracker with a scraper, logger, and notifier.

        Args:
            scraper (PriceScraper): The scraper used to fetch the current price.
            logger (PriceLogger): The logger used to record price history.
            notifier (EmailNotifier): The notifier used to send price drop emails.
        """
        self.scraper = scraper
        self.logger = logger
        self.notifier = notifier
        
    @Logger.log_execution 
    def track_price(self) -> None:
        """
        Checks the current product price, logs it, and sends an alert if the price matches the last logged price.
        """
        try:
            current_price = self.scraper.fetch_current_price()
            if current_price is not None:
                Logger.log_info(f"Fetched current price: ${current_price}")

                # Retrieve the last logged price
                last_logged_price = self.logger.get_last_logged_price()

                # Log the price if it’s not the same as the last logged price
                if last_logged_price > current_price:
                    self.logger.log_price(current_price)
                    self.notifier.send_price_alert(current_price, self.scraper.product_url)
                    Logger.log_info(f"Sent price drop alert for matching price: ${current_price}")
                else:
                    Logger.log_warning("No email sent as current price is not favoured")
            else:
                Logger.log_warning("Failed to retrieve the current price.")
        except Exception as e:
            Logger.log_error(f"Error in price tracking: {e}")




if __name__ == "__main__":
    # Configuration settings
    product_url = 'https://www.flipkart.com/apple-macbook-air-m2-8-gb-256-gb-ssd-mac-os-monterey-mlxw3hn-a/p/itmc2732c112aeb1?pid=COMGFB2GSG8EQXCQ&lid=LSTCOMGFB2GSG8EQXCQJWHH2F&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_1&otracker=browse&fm=organic&iid=351d22be-82a8-4155-bd44-722b6b8b6b14.COMGFB2GSG8EQXCQ.SEARCH&ppt=hp&ppn=homepage&ssid=de47plokzk0000001729842207317'  # Replace with the actual product URL
    price_history_file = 'price_history.csv'
    sender_email = '#####@gmail.com'
    receiver_email = '#####@gmail.com'
    email_password = '######'  # App password for 2FA
    smtp_server = "smtp.gmail.com"
    smtp_port= 587
    # Initialize components
    scraper = PriceScraper(product_url=product_url)
    logger = PriceLogger(price_history_file=price_history_file)
    notifier = EmailNotifier(sender_email, receiver_email, email_password,smtp_server,smtp_port)
    price_tracker = PriceTracker(scraper, logger, notifier)
    # Track and log price
    price_tracker.track_price()

    # Schedule the task to run every 1 hour
    Scheduler.schedule_task(tracker.track_price, interval_hours=1)
