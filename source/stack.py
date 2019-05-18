class Stack :
    '''
    A collection, meaning that it is a data structure that contains multiple elements.
    '''
    def __init__(self):
        '''
        Initialize a new empty stack.
        '''
        self.items = []

    def push(self, item):
        '''
        Add a new item to the stack.
        '''
        self.items.append(item)

    def pop(self):
        '''
        Remove and return an item from the stack. The item that is returned is always the last one that was added.
        '''
        return self.items.pop()

    def is_empty(self):
        '''
        Check whether the stack is empty.
        '''
        return (self.items == [])
