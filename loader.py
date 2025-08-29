import os
from data.config import HOST, USER, PASSWORD, DB
import logging
from db.database import Database


db = Database(
    host=HOST, user=USER, password=PASSWORD, db=DB
)


# root_logger = logging.getLogger()
# format = "%(filename)s - %(funcname)s - %(lineno)s - %(message)s"
# formater = logging.Formatter(format)


# log_file = 'log/logging.log'

# if not os.path.exists(log_file):
#     os.mkdir(log_file)


# file_logger = logging.FileHandler(log_file)
# file_logger.format(formater)

# root_logger.addHandler(file_logger)