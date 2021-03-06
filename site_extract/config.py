#!/usr/bin/python
# -*- coding: utf8 -*-
"""
 Create by Nicolas Drufin
 Last modified: dec 2014
 Description: Class to add config
"""

from ConfigParser import ConfigParser
import os
import re

class Config():
    """
    Class inherit from ConfigParser
    """
    def __init__(self, path):
        """
        Constructor
        """
        self._cfparser = ConfigParser()
        #open filepath
        try:
            self._cfparser.readfp(open(path, 'r'))
        except: 
            print "Unable to read cfg file", path
            
    def get_sites_info(self):
        """
        Get dic with site info by section
        """
        sites = {}
        for site in self._cfparser.sections():
            sites[site] = self._get_site_section_info(site)
        return sites
        
    def _get_site_section_info(self, sitesection):
        """
        Get dic with site info
        """
        siteinfos = {}
        for (k, v) in self._cfparser.items(sitesection):
            #format regex
            if "re_" in k:
                v = re.compile(r'%s'%v, re.I)
            elif "int_" in k:
                v = int(v)
            #add to dict
            siteinfos[k] = v
        return siteinfos
        
    def __getitem__(self, key):
        """
        Redirect __getitem__ func
        """
        dic = {}
        for k, v in self._cfparser.items(key):
            dic[k] = v
        return dic