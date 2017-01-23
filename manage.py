#!/usr/bin/env python
import os
import sys
import schedule
import time
import threading
from threading import Thread
from time import sleep
from factbot import scrapeFacts
# import django

keepGoing = True

# def job():
#     print("I'm working...")

schedule.every().day.at("09:34").do(scrapeFacts)
# schedule.every(10).seconds.do(scrapeFacts)

def runScheduler():
    while keepGoing:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    thread = Thread(target = runScheduler)
    thread.start()
    #time.sleep(5)
    # keepGoing = False
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fact_bot.settings")
    # django.setup()
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
