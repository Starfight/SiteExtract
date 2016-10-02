# -*- coding: utf8 -*-
# Copyright 2016 Nicolas DRUFIN
# Configure logger

import logging

def setup_logger(name="siteextract", debug=False, verbose=False, to_console=False):
    """
    Setup logging
    :param name: Loger name
    :param debug: Enable debug messages
    :param quiet: Disable verbose mode
    :param to_console: Enable Streamhandler instead of Filehandler
    """

    # setup level
    level = logging.CRITICAL
    if debug:
        level = logging.DEBUG
    elif verbose:
        level = logging.INFO

    # create loger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # setup handler
    if to_console:
        handler = logging.StreamHandler()
    else:
        handler = logging.FileHandler("logs/{0}.log".format(name))
    handler.setLevel(level)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S")

    # add formatter to handler
    handler.setFormatter(formatter)

    # add handler to logger
    logger.addHandler(handler)

    # set defaut logger
    logging.root = logger

