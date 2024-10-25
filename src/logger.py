import logging
import inspect

class Logger:
    """
    A simple logger class to log messages with the module and function name.
    """

    @staticmethod
    def setup_logging():
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    @staticmethod
    def log_info(message: str):
        logging.info(message)

    @staticmethod
    def log_warning(message: str):
        logging.warning(message)

    @staticmethod
    def log_error(message: str):
        logging.error(message)

    @staticmethod
    def log_execution(func):
        """
        Decorator that logs the execution of the function, including module and function name.
        """
        def wrapper(*args, **kwargs):
            module_name = inspect.getmodule(func).__name__
            Logger.log_info(f"Executing '{func.__name__}' in module {module_name}")
            return func(*args, **kwargs)
        return wrapper

# Set up logging configuration
Logger.setup_logging()
