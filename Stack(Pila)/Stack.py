from Node import *

class Stack:
    __anchor = None
    __work = None    
    
    def __init__(self):
        self.__anchor = Node()
        self.__work = Node()
        
        self.__anchor.set_next(None)
    
    def push(self, data):
        temp = Node()
        temp.set_data(data)
        
        temp.set_next(self.__anchor.get_next())
        self.__anchor.set_next(temp)
    
    def pop(self):
        value = 0
        
        if self.__anchor.get_next() != None:
            self.__work = self.__anchor.get_next()
            value = self.__work.get_data()

            self.__anchor.set_next(self.__work.get_next())
            self.__work.set_next(None)
        
        return value
    
    def peek(self):
        value = 0
        
        if self.__anchor.get_next() != None:
            self.__work = self.__anchor.get_next()
            value = self.__work.get_data()
            
        return value
        
    def transverse(self):
        self.__work = self.__anchor
        
        while self.__work.get_next() != None:
            self.__work = self.__work.get_next()
            print(self.__work.show())