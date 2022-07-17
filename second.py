#Первая реализация
#Добавление элемента за O(1)
#Удаление элемента за O(1)
class Circular_queue():
    """Circular queue class"""
    def __init__(self, size=10):
        self.queue = [None]*size
        self.tail = 0
        self.head = -1
        self.max_size = size

    def append(self, value, overwright = False):
        """Append value to the end of buffer"""
        
        if self.is_full() and self.head != -1:
            if overwright:
                self.tail = (self.tail + 1)%self.max_size
            else:
                raise OverflowError('Buffer is full, unable to append new element')
        self.head = (self.head + 1)%self.max_size
        self.queue[self.head] = value

    def is_empty(self):
        """Check if buffer is empty"""
        return self.queue[self.tail] is None
    
    def is_full(self):
        """Check if buffer is full"""
        return (self.tail - self.head)%self.max_size == 1
    
    def pop(self):
        """Pop the element added first"""
        if self.is_empty():
            raise Exception('Pop from empty buffer')
        self.queue[self.tail] = None
        self.tail = (self.tail + 1)%self.max_size
        
    def clear(self):
        """Clear buffer"""
        self.queue = Circular_queue(self.max_size).queue
    
    def __repr__(self):
        return repr(self.queue)
    
    def __getitem__(self, index):
        return self.queue[index]
        

#Вторая реализация
#Добавление элемента за O(n)
#Удаление элемента за O(1)
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return repr(self.value)
    
class Circular_queue_2:
    
    def __init__(self, max_size = 10):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.cur_size = 0
        
    def append(self, value, overwright = False):
        """Append value to buffer"""
        temp = self.head

        if temp is None:
            self.head = self.tail = Node(value, self.head)
            return

        while temp != self.tail:
            temp = temp.next_node
        
        if self.cur_size < self.max_size:
            temp.next_node = Node(value, self.head)
            self.tail = temp.next_node
            self.cur_size += 1
        elif overwright:
            self.tail = self.head
            self.tail.value = value
            self.head = self.head.next_node
        else:
            raise OverflowError('Buffer is full, unable append new element')

    def pop(self):
        """Pop the element edded first"""
        if self.cur_size > 1:
            temp = self.head.next_node
            del self.head
            self.head = self.tail.next_node = temp
        else:
            del self.head
        self.cur_size -= 1
    
    def __repr__(self):
        return str(list(self.__iter__()))
    
    def __iter__(self):
        temp = self.head
        while True:
            yield temp.value
            temp = temp.next_node

            if temp == self.head:
                break


#Третья реализация
#Добавление элемента за O(1)
#Удаление элемента за O(1)
#Бытсрее остальных реализаций
from collections import deque

class Circular_Queue_3:
    def __init__(self, max_size):
        self.queue = deque(maxlen=max_size)
        self.max_size = max_size

    def append(self, value, overwright = False):
        if overwright:
            self.queue.append(value)
        elif len(self.queue) < self.max_size:
            self.queue.append(value)
        else:
            raise OverflowError('Buffer is overflowed, unable to append new element')

    def pop(self):
        self.queue.pop()
    
    def __repr__(self):
        return repr(self.queue)
