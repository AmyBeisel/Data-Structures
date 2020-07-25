"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    """
    Optional `delete` method on `ListNode` to make subsequent
    methods more DRY.
    """

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            #1 <--> 2 <--> 3
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    #create a new node
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        #increment the length
        self.length +=1
        #if the DLL is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        #if the DLL is not empty
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #get the value
        value = self.head.value
        #delete the node
        self.delete(self.head)
        return value
        
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #create a new node
        new_node = ListNode(value, None, None)
        #increment the length
        self.length += 1
        #if the DLL is empty
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        #if the DLL is not empty
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        #get the value
        value = self.tail.value
        #delete the node
        self.delete(self.tail)
        return value
        
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #if only one node in list
        if node is self.head:
            return
        #get the value
        value = node.value
        self.delete(node)
        self.add_to_head(value)
        # if node is self.tail:
        #     self.remove_from_tail()
        # else:
        #     node.delete()
        #     self.length -= 1
        # self.add_to_head(value)
        
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        #get the value
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        #if list is empty
        if not self.head and not self.tail:
            return None
        #if 1 node
        if self.head == self.tail:
            self.head = self.tail = None
        #if the node is the head
        if node == self.head:
            self.head = node.next
            self.head.prev = None
        #if the node is the tail
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        #if the node is somewhere in the middle
        else:
            node.delete()
        self.length -= 1

        

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_value = self.head.value
        current_node = self.head

        #walk through the entire list
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value