#!/usr/bin/python
# -*- coding: utf8 -*-
"""
 Create by Nicolas Drufin
 Last modified: dec 2014
 Description: Class to extract one site
"""

import urllib2
from site_extract.site.articlestruct import ArticleStruct

class SiteExtract:
    """
    Class to extract site
    """
    REPLACE_TXT = "@SEARCH@"
    PAGE_NUMBER_TXT = "@PAGE_NUMBER@"
    ARTICLESPERPAGE_TXT = "@ARTICLESPERPAGE@"
    
    def __init__(self, sitename, siteinfos):
        """
        Constructor
        """
        self._sitename = sitename
        self._siteinfos = siteinfos
        
        #test
        result = self.get_page_search("table")
        for url in self.get_article_links(result):
            print url
            print self.get_article_info(url)
    
    def get_page_search(self, keyword):
        """
        Research a keyword on the page and return page result
        """
        #Format adress
        reqAdress = self._siteinfos.get("url_research")
        reqAdress = reqAdress.replace(self.REPLACE_TXT, keyword)
        reqAdress = reqAdress.replace(self.PAGE_NUMBER_TXT, "1")
        reqAdress = reqAdress.replace(self.ARTICLESPERPAGE_TXT, str(self._siteinfos.get("int_articlesperpage")))
        
        # send request adress
        result = urllib2.urlopen(reqAdress)
        return result.read().decode('utf-8')
        
    def get_nb_pages(self, page):
        """
        Return page number for current search
        """
        pattern = self._siteinfos.get("re_articlesnumber")
        nbarticlesperpage = self._siteinfos.get("int_articlesperpage")
        #search number of article
        m = pattern.search(page)
        if m is None:
            return
        #convert to int
        try:
            nbarticles = int(m.group(1))
        except:
            return
        #divide by article per page number
        nbpage = nbarticles / nbarticlesperpage + 1
        return nbpage
        
    def get_article_links(self, page):
        """
        Return current page article links as a list
        """
        pattern = self._siteinfos.get("re_articlelink")
        sitebase = self._siteinfos.get("url_site")
        #get link list of all product on the page and add site url to href
        linklist = []
        for m in pattern.finditer(page):
            linklist.append(sitebase+m.group(1))
        #delete doublons in list
        linklist = list(set(linklist))
        return linklist
        
    def get_article_info(self, url):
        """
        Return information for an article url
        """
        # send request adress
        page = urllib2.urlopen(url)
        page = page.read().decode('utf-8')
        
        # search info about article
        dicInfos = ArticleStruct()
        for info in dicInfos.INFOARTICLE.keys():
            pattern = self._siteinfos.get("re_"+info)
            res = pattern.search(page)
            if not res is None:
                for i in range(1, pattern.groups+1) :
                    if not res.group(i) is None:
                        res = res.group(i)
                        break
            dicInfos[info] = res
        
        #return dic result
        return dicInfos
        
    def debug_site(self, page):
        file = open("sitedebug.html", "w")
        file.write(page)
        file.close()
                