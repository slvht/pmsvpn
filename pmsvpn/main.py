#!/usr/bin/env python3

import argparse
import logging
import logging.handlers
import sys
import time

logger = logging.getLogger(__name__)

from pmsvpn.pyssh import SSHClient

def configure_logging():
    root_logger = logging.getLogger()
    handler = logging.StreamHandler()
    # handler = logging.handlers.SysLogHandler('/dev/log')
    formatter = logging.Formatter(
        '%(asctime)s ' + ' appname ' + '%(filename)s %(name)-15s %(levelname)-4s %(message)s',
        '%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)


def main(args):
    configure_logging()
    logger.info('Started runnning')

    while True:
        logger.info('Beep...')
        time.sleep(5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Python Seed',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    main(parser.parse_args())
