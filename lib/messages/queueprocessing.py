#!/usr/bin/python
# -*- coding: utf8 -*-
"""
 Create by Nicolas Drufin
 Created: jan 2014
 Description: Queue processing
"""
from multiprocessing import Process, Queue

class QueueProcessing():
    """
    Queue processing message from sites to mysql database
    """
    
    def __init__(self):
        """
        Constructor
        """
        self._queue = Queue()
        self._subscriberList = []
        self._ownprocess = Process(self.release_entry, args=self._queue)
        # Start processing
        self._running = True
        self._ownprocess.start()
        
    def release_entry(self, queue):
        """
        Release message to all subscribers
        """
        while self._running:
            # Tant que la queue contient des entrées
            while not queue.empty():
                entry = queue.get()
                #Essayer d'envoyer la donnée, sinon remettre dans la pile
                try:
                    for method in self._subscriberList:
                        if not method(entry):
                            raise
                except:
                    queue.put(entry)
                    
    def put_entry(self, entry):
        """
        Put a entry in queue
        """
        try:
            queue.put(entry)
            return True
        except:
            return False
        
    def subscribe(self, method):
        """
        Add subscriber to releaseEntry
        Method need a entry arg and return True is message receive
        """
        self._subscriberList.append(method)
    
    def unsubscribe(self, method):
        """
        Remove subscriber to releaseEntry
        """
        if self._subscriberList.count(method):
            self._subscriberList.remove(method)
            
    def stop_queue(self):
        """
        Stop all processing 
        Warning: data may be lost !
        """
        self._running = False
        self._ownprocess.join()