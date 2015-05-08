#!/usr/bin/python
# -*- coding: utf8 -*-
"""
 Create by Nicolas Drufin
 Last modified: jan 2015
 Description: Struct class for article data
"""
import cgi 

class ArticleStruct(dict):
    """
    Struct class for article data
    """
    INFOARTICLE = {"name":str, 
                   "price":float,
                   "img":str, 
                   "width":float, 
                   "height":float, 
                   "lenght":float, 
                   "color":str, 
                   "ref":str}
    
    def __init__(self):
        """
        Constructor
        """
        super(ArticleStruct, self).__init__()
        for info, typeinfo in self.INFOARTICLE.items():
            self[info] = typeinfo()
            
    def __setitem__(self, key, value):
        """
        Rewrite setitem func
        """
        if key in self.INFOARTICLE.keys():
            if type(value) is str:
                value = cgi.escape(value)
            try:
                value = self.INFOARTICLE[key](value)
            except:
                value = 0
                
            # Fonction parent (dict)
            super(ArticleStruct, self).__setitem__(key, value)
            
    def get_items_tuple_string(self):
        """
        Return items in a tuple as a string (insert in musql db)
        """
        return str(tuple(self.values()))