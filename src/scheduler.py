import schedule
import time
from logger import Logger

class Scheduler:
    """
    A class to manage scheduling of tasks at regular intervals.

    Methods:
        schedule_task(task, interval_hours): Schedules the given task to run every specified hours.
    """

    @Logger.log_execution
    def schedule_task(task, interval_hours: int = 1):
        """
        Schedules the given task to run at a specified interval (in hours).

        Args:
            task (callable): The task to be scheduled.
            interval_hours (int): The interval in hours at which the task should run (default is 1 hour).
        """
        schedule.every(interval_hours).hours.do(task)
        logging.info(f"Scheduled task every {interval_hours} hours.")
        while True:
            schedule.run_pending()
            time.sleep(1)
