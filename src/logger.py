import logging
import inspect

class Logger:
    """
    A logger class with color-coded logs for different levels (info, warning, error),
    showing module and function names.
    """

    # Define ANSI color codes
    COLORS = {
        'INFO': '\033[94m',    # Blue
        'WARNING': '\033[93m', # Yellow
        'ERROR': '\033[91m',   # Red
        'RESET': '\033[0m'     # Reset to default
    }

    @staticmethod
    def setup_logging():
        # Configure logging with a custom formatter that uses color codes
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        # Set up custom handlers if more complex handling is needed in future

    @staticmethod
    def format_message(level: str, message: str) -> str:
        """
        Adds color to the message based on the log level.

        Args:
            level (str): The log level as a string.
            message (str): The message to log.
        
        Returns:
            str: The formatted message with color codes.
        """
        color = Logger.COLORS.get(level, Logger.COLORS['RESET'])
        reset = Logger.COLORS['RESET']
        return f"{color}{message}{reset}"

    @staticmethod
    def log_info(message: str):
        logging.info(Logger.format_message('INFO', message))

    @staticmethod
    def log_warning(message: str):
        logging.warning(Logger.format_message('WARNING', message))

    @staticmethod
    def log_error(message: str):
        logging.error(Logger.format_message('ERROR', message))

    @staticmethod
    def log_execution(func):
        """
        Decorator that logs the execution of the function, including module and function name.
        """
        def wrapper(*args, **kwargs):
            module_name = inspect.getmodule(func).__name__
            Logger.log_info(f"Executing '{func.__name__.upper()}' in module {module_name.upper()}")
            return func(*args, **kwargs)
        return wrapper

# Set up logging configuration
Logger.setup_logging()
