#!/usr/bin/python
# -*- coding: utf8 -*-
"""
 Create by Nicolas Drufin
 Last modified: dec 2014
 Description: Engine for extract and save data in database
"""

from lib.database.mysql import Mysql
from lib.config import Config
from lib.site.siteextract import SiteExtract
from lib.site.articlestruct import ArticleStruct

class ExtractEngine():
	"""
	Class to extract site infos
	"""
	def __init__(self, paramcfgpath, sitecfgpath):
		"""
		Constructor
		"""
		# open config files
		self._paramcfg = Config(paramcfgpath)
		self._sitecfg = Config(sitecfgpath)
		
		# create db connexion
		self._mysql = Mysql(self._paramcfg["MYSQL"]["host"], self._paramcfg["MYSQL"]["user"], self._paramcfg["MYSQL"]["password"], self._paramcfg["MYSQL"]["database"])
		self._insert_product = "INSERT INTO "+self._paramcfg["MYSQL"]["tableproduct"]+" VALUES {}"
		
		# create site extract
		self.sitelist = []
		for site, cfg in self._sitecfg.getSitesInfo().items():
			se = SiteExtract(site, cfg)
			
		
	def processSitesExtract(self):
		"""
		Run sites extract
		"""
		for site in self.sitelist:
			pass
			
	def processEntry(self, entry):
		"""
		Insert/Update data in Mysql database
		"""
		insertquery = self._insert_product.format(entry.getItemsTupleString())
		try:
			self._mysql.query(insertquery)
			return True
		except:
			return False