import logging
import sys, os
from logging.handlers import TimedRotatingFileHandler
from time import sleep

FORMATTER = logging.Formatter("%(asctime)s – %(levelname)s — %(name)s — %(message)s")
LOG_FILE = ".\\logs\\log"
PATCH_DIR = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")

def get_filename(filename):
    log_directory = os.path.split(filename)[0]
    date = os.path.splitext(filename)[1][1:]
    filename = os.path.join(log_directory, date)
    if not os.path.exists('{}.log'.format(filename)):
        return '{}.log'.format(filename)
    index = 0
    f = '{}.{}.log'.format(filename, index)
    while os.path.exists(f):
        index += 1
        f = '{}.{}.log'.format(filename, index)
    return f

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler

def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='W0', delay=True)
    file_handler.suffix = '%Y-%m-%d'
    file_handler.namer = get_filename
    file_handler.setFormatter(FORMATTER)
    return file_handler

def get_console_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    return logger

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    return logger

def get_file_logger(filename, module):
    logger = logging.getLogger(module)
    logger.setLevel(logging.INFO)
    f = logging.FileHandler("%s/logs/%s.log" % (PATCH_DIR, filename))
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    f.setFormatter(formatter)
    logger.addHandler(f)
    return logger
