# logger handlers are responsible for the outputs via mails,https etc.....

import logging

logger = logging.getLogger(__name__)

# define the handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file_handler.log')

# define the level and the format to be used
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

# set the formatters
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning('warning here')
logger.error('error here')

