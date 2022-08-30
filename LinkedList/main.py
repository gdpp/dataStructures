
from LinkedList import LinkedList

# main program...
if __name__ == "__main__":
    my_linked_list = LinkedList()
    
    my_linked_list.add(1)
    my_linked_list.add(2)
    my_linked_list.add(3)
    my_linked_list.add(4)
    my_linked_list.add(5)
    my_linked_list.add(6)
    
    my_linked_list.transverse()
    
    print(my_linked_list.is_empty())
    
    my_linked_list.empty()
    
    my_linked_list.transverse()
    
    print(my_linked_list.is_empty())
    
    my_linked_list.add(7)
    my_linked_list.add(8)
    my_linked_list.add(9)
    my_linked_list.add(10)
    my_linked_list.add(11)
    
    print(bool(my_linked_list.search(11)))
    print(bool(my_linked_list.search(100)))
    
    print(my_linked_list.search_index(9))
    print(my_linked_list.search_index(11))
    
    previous = my_linked_list.search_previous(11)
    print(previous.get_data())
    
    my_linked_list.delete(8)
    
    my_linked_list.transverse()
    
    my_linked_list.empty()
    
    print("-------------------")
    my_linked_list.add(2)
    my_linked_list.add(6)
    my_linked_list.add(3)
    my_linked_list.add(17)
    my_linked_list.add(15)
    my_linked_list.add(8)
    my_linked_list.add(4)
    
    my_linked_list.transverse()
    
    
    my_linked_list.insert(17, 100)
    
    print("-------------------")
    my_linked_list.transverse()
    
    my_linked_list.insert_begin(3000)
    my_linked_list.insert_begin(2000)
    my_linked_list.insert_begin(1000)
    
    print("-------------------")
    my_linked_list.transverse()
    
    
    print(my_linked_list.get_by_index(1))
    
    print(my_linked_list.quantity())