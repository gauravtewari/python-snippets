#!/tool/pandora64/hdk-6/1/bin/python3 -O

"""
    # see webpage https://docs.python.org/3/howto/logging.html
    # setting a level means everything including that level and above will be printed.
    # For example setting level to WARNING will print logging.warning(), logging.error(), logging.critical(), logging.exception()
    # setting level to ERROR will print logging.error(), logging.critical(), logging.exception()
    # setting level to DEBUG will print all

Sample Usage:
Assuming we get the log level from cmd line using argparse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-l","--log", dest='log_level', help="set log level", default='WARNING', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
args=parser.parse_args()

# set the level based on the command line info passed, default is warning
setup_logging(args.log_level)

logging.warning("Watch Out!!")
logging.debug("Debug info!")
logging.info("Just Info!")
logging.error("Error")
logging.critical("Critical")
"""

# set logging info
import logging
def setup_logging(log_level):
    # deduce the numaric log level from string log level
    log_level_num = getattr(logging, log_level.upper(), None)
    if not isinstance(log_level_num, int):
        raise ValueError('Invalid log level: %s' % log_level)

    logging.basicConfig(format='%(levelname)s: %(message)s', level=log_level_num) # only first call will do soemthing, other calls to basicConfig will be noops
