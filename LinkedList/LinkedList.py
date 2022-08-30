from Node import *

class LinkedList:
    
    # Header of the linked list
    __anchor = None
    
    # reference variable help us to work with the list
    __work = None
    __work2 = None
    
    def __init__(self):
        self.__anchor = Node()
        self.__work = Node()
        
        self.__anchor.set_next(None)
    
    # Iterate whole the linked list
    def transverse(self):
        # Work at the begining
        self.__work = self.__anchor
        
        # Iterate until found the None
        while self.__work.get_next() != None:

            # Moving foward work1
            self.__work = self.__work.get_next()
            
            # Getting data and show it
            print(self.__work.show())

    def add(self, data):
        # Work at the begining
        self.__work = self.__anchor
        
        # Iterate until found the end
        while self.__work.get_next() != None:
            self.__work = self.__work.get_next()
        
        # Create new node
        temp = Node()
        
        # Assign data
        temp.set_data(data)
        
        # Finish correctly
        temp.set_next(None)

        # Linking the last node found with the new one
        self.__work.set_next(temp)
        
    def empty(self):
        self.__anchor.set_next(None)
    
    def is_empty(self):
        if self.__anchor.get_next() == None:
            return True
        else:
            return False
    
    def search(self, data):
        if self.is_empty() == True:
            return None
        
        self.__work2 = self.__anchor
        
        while self.__work2.get_next() != None:
            self.__work2 = self.__work2.get_next()

            if self.__work2.get_data() == data:
                return self.__work2
        
        # Not found    
        return None

    # Return index of Node
    def search_index(self, data):
        result = -1
        
        self.__work = self.__anchor
        
        while self.__work.get_next() != None:
            self.__work = self.__work.get_next()
            result += 1
            
            if self.__work.get_data() == data:
                return result
        
        return -1

    # Found previous node
    # If it's found in the first node, returns the anchor
    # if not's found returns the last node
    def search_previous(self, data):
        self.__work2 = self.__anchor
        
        while self.__work2.get_next() != None and self.__work2.get_next().get_data() != data:
            self.__work2 = self.__work2.get_next()
        
        return self.__work2

    # Delete the first data match
    def delete(self, data):
        # if null finish the function
        if self.is_empty() == True:
            return
        
        # Search the nodes with what we will work
        previous = self.search_previous(data)
        found = self.search(data)
        
        # If not found node to delete finish the function
        if found == None:
            return
        
        # Jump node
        previous.set_next(found.get_next())
        
        # Delete teh current node from the list
        found.set_next(None)
        
    # Insert node
    def insert(self, curr, data):
        #Search insert position
        self.__work = self.search(curr)
        
        if self.__work == None:
            return
        
        # Create temp node
        temp = Node()
        temp.set_data(data)
        
        # Connect temp node to the list
        temp.set_next(self.__work.get_next())
        
        # Connect work node to temp
        self.__work.set_next(temp)
    
    def insert_begin(self, data):
        # Create temp node
        temp = Node()
        temp.set_data(data)
        
        # Connect temp node to the anchor
        temp.set_next(self.__anchor.get_next())
        
        # Connect anchor node to temp
        self.__anchor.set_next(temp)
    
    def get_by_index(self, i):
        self.__work2 = None
        index = -1
        
        self.__work = self.__anchor
        
        while self.__work.get_next() != None:
            self.__work = self.__work.get_next()
            index += 1
            
            if index == i:
                self.__work2 = self.__work
        
        return self.__work2

    def quantity(self):
        n = 0

        self.__work = self.__anchor
        
        while self.__work.get_next() != None:
            self.__work = self.__work.get_next()
            n += 1
        
        return n