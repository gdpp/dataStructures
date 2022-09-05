from Stack import Stack

# main program...
if __name__ == "__main__":
    pila = Stack()
    
    pila.push(5)
    pila.push(3)
    pila.push(10)

    pila.transverse()

    print(pila.pop())

    pila.transverse()

    print(pila.peek())
    print(pila.peek())
    
    pila.transverse()