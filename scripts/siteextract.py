#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import sys
from optparse import OptionParser
from site_extract.extractengine import ExtractEngine

def main(argv):
    # parse arguments options
    parser = OptionParser()
    parser.add_option("-c", "--conf", dest="config_file", help="Configuration file")
    # TODO: remove this config file and store sites conf in database
    parser.add_option("-s", "--sites", dest="sites_file", help="Sites configuration file")
    (options, args) = parser.parse_args()

    # verify options
    if not options.config_file:
        print "Error: No configuration file defined"
        return 1

    # start engine
    engine = ExtractEngine(options.config_file, options.sites_file)

if __name__ == "__main__":
    sys.exit(main(sys.argv))