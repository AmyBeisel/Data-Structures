from collections import deque

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        #current node's value
        self.value = value
        #less than value
        self.left = None
        #greater than value
        self.right = None

    #Insert the given value into the tree
    def insert(self, value):
        #check if new node's value is less than current node's value. 
        if value < self.value:
            if not self.left: #there is no self.left
                self.left = BSTNode(value) #now making a node (not empty)
            else:
                self.left.insert(value) #inserting value
        #check whether new node's value is greater than or equal to the current's node's value
        if value >= self.value:
            if not self.right: #there is no self.right
                self.right = BSTNode(value) #creating a node 
            else:
                self.right.insert(value) #inserting the value
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #check whether current node matches target. 
        if self.value == target:
            return True
        # is the target lower than the value?
        if target < self.value:
            #is there any child node?
            if not self.left:
                return False
            #if there is a node on the right, start the function over. 
            else:
                return self.left.contains(target)
        else:
            #is there any child node?
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        # self.left.value will always be smaller than the root
        # so we have to check only the self.right path
        # U: traverse (travel) BST to find the global max
        #1. check your input --> is there a node here?
        #2.declare max variable == self.value
        #3. iterate through the tree until we hit NULL
        #4.  Update max_value 
        #5. move to the right
        #ITERATIVE SOLUTION
        
        # if not self:
        #     return None
        # max_value = self.value
        # current = self
        # while current:
        #     if current.value > max_value:
        #         max_value = current.value
        #     current = current.right
        # return max_value

        #RECURSIVE SOLUTION
        #base case: no right node available
        # recursive step: pass right subtree to get_max
        if not self.right:
            return self.value
        else:
            return self.right.get_max()
            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #U: apply fn to each node of the tree
        # 1. apply the root
        #2. call for_each on the left and right side of tree. 
        #call the function `fn`
        fn(self.value)
        print(self.value)
        #go to the left node if any
        if self.left:
            print('left')
            self.left.for_each(fn)
        #go to the right node if any
        if self.right:
            print("right")
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node = None):
        if not self:
            return 
        # left --> root --> right
        if self.left:
            self.left.in_order_print()
        
        print(self.value)

        

        if self.right:
            self.right.in_order_print()
            

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node = None):
        #1. add root to the queue - define queue
        #2. process: pop node from the queue and print - add self to deque
        #3. add child nodes - iterate: while there are items in the qeque
        #4. dequeue/pop from the deque, point to result and print
        #5. add left and right childern to deque

        qq = deque()
        qq.append(self)

        while len(qq) > 0:
            current = qq.popleft()
            print(current.value)
            if current.left:
                qq.append(current.left)
            if current.right:
                qq.append(current.right)
            



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        s = []
        s.append(self)

        while len(s) > 0:
            current = s.pop()
            print(current.value)
            if current.left:
                s.append(current.left)
            if current.right:
                s.append(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        #0. check self
        #1. print self
        #   root --> left --> right
        #2. recurse to the left
        #3. recurse to the right
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        #0. check self
        
        #1. recurse to the left
        #2. recurse to the right
        #   left --> right --> root
        #3. print self
  
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
print("____")
bst.dft_print()


# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
