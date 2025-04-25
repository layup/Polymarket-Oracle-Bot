import os
import logging

from logging.handlers import RotatingFileHandler



file_name = 'basic.log'

file_path = os.path.join('logs', file_name)

# Log a message at the start of the program
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Max size of 10 MB
handler = RotatingFileHandler(file_path, maxBytes=10*1024*1024, backupCount=5)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

logger.warning(f"Logging started with filename: {file_name}, level: {logger.level}")
