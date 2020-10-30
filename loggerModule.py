# Logging 

import logging

logger = logging.getLogger(__name__)
# you can propagate loggers to stop from basing to the root
logger.propagate = False # nothing wil now be logged to the main file
logger.info('Logging no from the root but logger module')

# call it from the main module, you can comment out the prorpagate to get the output
