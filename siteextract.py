#!/usr/bin/python
# -*- coding: utf8 -*-

from lib.extractengine import ExtractEngine
import os

PARAM = "conf"+os.sep+"param.cfg"
SITES = "conf"+os.sep+"sites.cfg"

def start_extract():
    engine = ExtractEngine(PARAM, SITES)
    

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    #TODO load config file and some arg
    start_extract()