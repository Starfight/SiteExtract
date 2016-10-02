#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
import logging
from optparse import OptionParser
from site_extract.extractengine import ExtractEngine
from site_extract.logs import setup_logger

def main(argv):
    # parse arguments options
    parser = OptionParser()
    parser.add_option("-c", "--conf", type="string", dest="config_file", help="Configuration file")
    parser.add_option("-q", "--quiet", action="store_false", dest="verbose")
    parser.add_option("-d", "--debug", action="store_true", dest="debug")
    # TODO: remove this config file and store sites conf in database
    parser.add_option("-s", "--sites", type="string", dest="sites_file", help="Sites configuration file")
    (options, args) = parser.parse_args()

    # setup logger
    setup_logger(debug=options.debug, verbose=options.verbose, to_console=options.debug)

    # verify options
    if not options.config_file:
        logging.critical("No configuration file defined")
        return 1

    # start engine
    engine = ExtractEngine(options.config_file, options.sites_file)

if __name__ == "__main__":
    sys.exit(main(sys.argv))