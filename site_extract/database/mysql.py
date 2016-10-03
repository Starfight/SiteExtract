#!/usr/bin/python
# -*- coding: utf8 -*-
"""
 Create by Nicolas Drufin
 Last modified: dec 2014
 Description: Class to manage Mysql database connection
"""

import time
import pymysql
from multiprocessing import Process
import traceback
import logging

class Mysql:
    """
    Class to manage Mysql database connection
    """
    
    def __init__(self, host, user, password, database):
        """
        Constructor
        """
        #parameters
        if ':' in host:
            self._host, self._port = host.split(':')
            self._port = int(self._port)
        else:
            self._host = host
            self._port = 3306
        self._user = user
        self._password = password
        self._database = database
        #db object
        self._dbconnection = None
        #connection state
        self._running = True
        self._connected = False
        # start connection
        self._connProcess = Process(target=self.connect)
        self._connProcess.start()
        
    def connect(self):
        """
        Connect to database
        """
        while self._running:
            if not self._connected:
                try:
                    self._dbconnection = pymysql.connect(host=self._host, port=self._port, user=self._user, passwd=self._password, db=self._database)
                    self._connected = True
                    logging.info("Connection to database {0} on host {1} has been establish".format(self._database, self._host))
                except:
                    self._connected = False
                    logging.critical("Unable to connect to database {0} on host {1}".format(self._database, self._host))
                    logging.debug(traceback.print_exc())
                    time.sleep(2) 
            else:
                try:
                    if self._dbconnection.ping():
                        time.sleep(10) 
                    else:
                        self._connected = False
                except:
                    self._connected = False
                    logging.critical("Unable to ping database {0} on host {1}".format(self._database, self._host))
                    time.sleep(2)

        # close when leaving the loop
        self._dbconnection.close()
        logging.info("Connection to database {0} on host {1} has been closed".format(self._database, self._host))
                
    def query(self, query):
        """
        Execute a query on mysql server
        """
        # Si on est connecté
        if self._connected:
            #Crée le curseur avec un type dict
            cursor = self._dbconnection.cursor(pymysql.cursors.DictCursor)
            try:
                # Exécute la requête (None si vide)
                if cursor.execute(query):
                    res = cursor.fetchall()
                    cursor.close()
                    return res
            except Exception as e:
                logging.critical("Error during query {0}: {1}".format(query, repr(e)))
                logging.debug(traceback.print_exc())
        return None
            
    def disconnect(self):
        """
        Deconnecte le server MySQL
        """
        self._running = False
        self._connProcess.join()
        self._connected = False