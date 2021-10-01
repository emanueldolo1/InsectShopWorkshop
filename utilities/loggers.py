import sys
import logging
import time
from utilities import config


def log_message(message):
    stream_handler = logging.StreamHandler(sys.stdout)
    logger = __setup_logger(stream_handler)

    timestamp = time.strftime("%d/%m/%Y %H:%M:%S")

    if config.REPORT:
        message = "<b>" + message + "</b>"
        p_html_tag = "<p>{}: {}</p>".format(timestamp, message)
        logging.getLogger().info(p_html_tag)

    else:
        logging.getLogger().info(timestamp + ": " + message)

    logger.removeHandler(stream_handler)


def log_screenshot(image_path):
    stream_handler = logging.StreamHandler(sys.stdout)
    logger = __setup_logger(stream_handler)

    if config.REPORT:
        image_html_tag = '<img src={} height="135" width="240">'.format(image_path)
        link_html_tag = "<a href={}>{}</a>".format(image_path, image_html_tag)
        logging.getLogger().info(link_html_tag)

    logger.removeHandler(stream_handler)


def __setup_logger(stream_handler):
    logger = logging.getLogger()
    logger.level = logging.DEBUG
    logger.addHandler(stream_handler)
    return logger
