class Node:
    # Save data in the node
    __data = None
    
    # Reference variable used to point next node
    __next = None
    
    # Getters
    def get_data(self):
        return self.__data
    
    def get_next(self):
        return self.__next
    
    # Setters
    def set_data(self, data):
        self.__data = data
    
    def set_next(self, next):
        self.__next = next

    def show(self):
        return "[{}]".format(self.__data)