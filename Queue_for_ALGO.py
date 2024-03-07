# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 18:35:18 2024

@author: DWNeumann
"""


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
# print(q.isEmpty())

# q.enqueue(4)
# q.enqueue('dog')
# q.enqueue(True)


# print(q.size())
# print(q.isEmpty())

# q.enqueue(8.4)

# print(q.dequeue())
# (q.dequeue())

# # print(q.size())

q.enqueue("Unitas")
q.enqueue("Montana")
q.enqueue("Marino")
q.enqueue("Elway")
q.enqueue("Young")
q.enqueue("Favre")
q.size()
q.items
q.dequeue()

q.dequeue()
q.enqueue("Manning")
q.dequeue()
q.dequeue()
q.enqueue("Brady")
q.enqueue("Brees")
q.enqueue("Rodgers")
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.size()
q.items
