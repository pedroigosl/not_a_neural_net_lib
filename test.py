from typing import List
import logging
import time

log_date = str(time.strftime("%d-%m-%y_%H:%M:%S"))
log_name = f"logs/testlog_{log_date}.log"
logging.basicConfig(filename=log_name, filemode='w', level=logging.DEBUG)

logging.info('test')

logging.warning('test1')


logging.info('test2')

test3 = (f"Graph properties changed. New properties are:\n"
        f"reflexive:     {True}\n"
        f"symmetric:     {False}\n"
        f"transitive:    {True}")

logging.info(test3)
date = time.strftime("%d-%m-%y_%H:%M:%S")
print(date)