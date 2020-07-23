"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         # self.storage = ?
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size +=1
#         return self.storage.append(value)

#     def pop(self):
#         if self.size != 0:
#             self.size -= 1
#             return self.storage.pop()

# 2. Re-implement the Stack class, this time using the linked list implementation
#    as the underlying storage structure.
#    Make sure the Stack tests pass.

from singly_linked_list import LinkedList
class Stack():
    """Linked list as the underlying storage structure"""
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def pop(self):
        #!= : this mean there is no elements in the list 
        if self.size != 0:
            # -= : removing one element at a time.  
            self.size -= 1
            return self.storage.remove_tail()


