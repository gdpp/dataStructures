from Queue import Queue

if __name__ == '__main__':
    cola = Queue()

    cola.enqueue(5)
    cola.enqueue(3)
    cola.enqueue(7)
    cola.enqueue(1)

    cola.transverse()

    value = cola.dequeue()
    print(value)

    cola.transverse()

    cola.enqueue(8)

    cola.transverse()

    print(cola.peek())

    cola.transverse()