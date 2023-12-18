import asyncio
import time
from typing import Callable

import aioschedule as schedule
# https://github.com/ibrb/python-aioschedule

from Utils.logger import logger

""" Доделать!!! """

"""
Написать шедуллер запуска авто тестов из конфига
"""


class Schedule:
    def __init__(self, time_for_schedule: str,
                 job_func: Callable,
                 *args
                 ):
        self.time_for_schedule = time_for_schedule
        self.schedule = schedule
        self.set_schedule(job_func,
                          *args
                          )

    def set_schedule(self, job, *args):
        """ Получить шедуллер """

        self.schedule.every().monday.at(self.time_for_schedule).do(job, *args)
        self.schedule.every().tuesday.at(self.time_for_schedule).do(job, *args)
        self.schedule.every().wednesday.at(self.time_for_schedule).do(job, *args)
        self.schedule.every().thursday.at(self.time_for_schedule).do(job, *args)
        self.schedule.every().friday.at(self.time_for_schedule).do(job, *args)
        self.schedule.every().saturday.at(self.time_for_schedule).do(job, *args)
        self.schedule.every().sunday.at(self.time_for_schedule).do(job, *args)

    async def run_schedule(self):
        """ Запустить шедуллер """

        logger.info("Scheduler start")

        while True:
            await self.schedule.run_pending()
            time.sleep(12)


# for Tests
async def test_func(*args):
    logger.info("hi")
    for arg in args:
        logger.info(f"Другой аргумент из *argv: {arg}")


# Tests
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    s = Schedule("11:29", test_func, "1")
    loop.run_until_complete(s.run_schedule())


