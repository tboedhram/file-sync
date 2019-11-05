import os

import logging
import logging.handlers as handlers


def setup_log_directory():
    if not os.path.isdir('./logs/'):
        os.mkdir('./logs/')


def create_logger(name):
    setup_log_directory()
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    file_handler = handlers.TimedRotatingFileHandler(filename='logs/{name}.log'.format(name=name), encoding='UTF-8',
                                                     when='midnight')
    string_format = '%(asctime)s|%(levelname)s: %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    formatting = logging.Formatter(string_format, date_format)
    file_handler.setFormatter(formatting)
    logger.addHandler(file_handler)
    return logger
