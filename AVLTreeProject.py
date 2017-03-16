#Project #4
#Ismael Garrido Rodriguez
#Por

# AVLTree.py
from TreeNode import *

class AVLTree(object):

    #------------------------------------------------------------

    def __init__(self):

        '''post: creates empty AVL tree'''

        self.t = None

    #------------------------------------------------------------

    def insert(self, value):

        '''post: insert value into proper location in AVL tree'''

        self.t = self._insert_help(self.t, value)
    
    #------------------------------------------------------------
    def delete(self, value):
        """remove item from AVL tree
        post: item is removed from the tree"""
        
        self.t = self._delete_help(self.t, value)
    #------------------------------------------------------------

    def _insert_help(self, t, value):

        '''private helper method to insert value into AVL (sub)tree with
        root node t'''

        if t is None:
            t = TreeNode(value)
            
        elif value < t.item:
            t.left = self._insert_help(t.left, value)
            # left subtree height may be now larger than right subtree
            if get_height(t.left) - get_height(t.right) == 2:
                # determine which subtree the new value was inserted
                if value < t.left.item:
                    # insertion into left subtree of left child
                    t = self._left_single_rotate(t)
                else:
                    # insertion into right subtree of left child
                    t = self._right_left_rotate(t)

        elif value > t.item:
            t.right = self._insert_help(t.right, value)
            # right subtree height may be now larger than left subtree
            if get_height(t.right) - get_height(t.left) == 2:
                # determine which subtree the new value was inserted
                if value > t.right.item:
                    # insertion into right subtree of right child
                    t = self._right_single_rotate(t)
                else:
                    # insertion into left subtree of right child
                    t = self._left_right_rotate(t)

        else: 
            raise ValueError
            
        # update height of tree rooted at t
        t.height = max(get_height(t.left), get_height(t.right)) + 1
        return t

    #------------------------------------------------------------

    def _left_single_rotate(self, t):

        '''private rotation method for inserting into left subtree of
        left child of t'''

        grandparent = t
        parent = t.left

        grandparent.left = parent.right
        parent.right = grandparent
        t = parent

        grandparent.height = max(get_height(grandparent.left),
                                 get_height(grandparent.right)) + 1
        parent.height = max(get_height(parent.left), 
                            get_height(parent.right)) + 1
        return t

        
#---------------------------------------------------------------

    def _right_single_rotate(self, t):

        '''private rotation method for inserting into right subtree of
        right child of t'''

        grandparent = t
        parent = t.right

        grandparent.right = parent.left
        parent.left = grandparent
        t = parent

        grandparent.height = max(get_height(grandparent.right),
                                 get_height(grandparent.left)) + 1
        parent.height = max(get_height(parent.right), 
                            get_height(parent.left)) + 1

        return t
#------------------------------------------------------------

    def _right_left_rotate(self, t):

        '''private rotation method for inserting into right subtree of
        left child of t'''

        t.left = self._right_single_rotate(t.left)
        t = self._left_single_rotate(t)
        return t

                        
#------------------------------------------------------------

    def _left_right_rotate(self, t):

        '''private rotation method for inserting into left subtree of
        right child of t'''

        t.right = self._left_single_rotate(t.right)
        t = self._right_single_rotate(t)
        return t


 #------------------------------------------------------------
    def find(self, item):
        
        """ Search for item in AVL Tree
        post: Returns item from AVL Tree if found, None otherwise"""

        node = self.t
        while node is not None and not(node.item == item):
            if item < node.item:
                node = node.left
            else:
                node = node.right

        if node is None:
           raise ValueError
        else:
            print("The program has found ", node.item, "in the AVL Tree")
            return node.item


 #------------------------------------------------------------
    def _delete_help(self, t, value):

        '''private helper method to delete a value from AVL (sub)tree with
        root node t'''

        if t is None:   
           return None
        if value != t.item:
            raise ValueError

        elif value > t.item:                             # modify left
            t.left = self._delete_help(t.left, value)
            if get_height(t.right) - get_height(t.left) == 2:
                
                if value < t.right.item:
                    
                    t = self._left_single_rotate(t)
                else:
                    
                    t = self._right_left_rotate(t)

                t.height = max(get_height(t.left), get_height(t.right)) + 1
            
           
        elif value < t.item:                           # modify right
            t.right = self._delete_help(t.right, value)
            if get_height(t.left) - get_height(t.right) == 2:
                
                if value > t.left.item:
                    
                    t = self._right_single_rotate(t)
                else:
                    
                    t = self._left_right_rotate(t)
                    
                t.height = max(get_height(t.left), get_height(t.right)) + 1

             
        else:                                            # delete root
            if t.left is None:                        # promote right subtree
                t =  t.right
            elif t.right is None:                     # promote left subtree
                t = t.left
            else:

                t.item, t.left = self._delete_max(t.left)
                
                if value > t.item:
                    t.left = self._delete_help(t.left, value)
                    if get_height(t.right) - get_height(t.left) == 2:
                        if value < t.right.item:
                            t = self._right_single_rotate(t)
                        else:
                            t = self._left_right_rotate(t)

                elif value < t.item:
                    t.right = self._delete_help(t.right, value)
                    if get_height(t.left) - get_height(t.right) == 2:
                        if value > t.left.item:
                            
                            t = self._right_single_rotate(t)
                        else:
                            t = self._left_right_rotate(t)
                    t.height = max(get_height(t.left), get_height(t.right)) + 1
                
        return t

#------------------------------------------------------------
    def _delete_max(self, t):
        
        if t.right is None:          
            return t.item, t.left  
        else:
            # max is in right subtree, recursively find and delete it
            maxVal, t.right = self._delete_max(t.right)

            t.height = max(get_height(t.left), get_height(t.right)) + 1
            return maxVal, t  

#------------------------------------------------------------

    def __str__(self):
        if self.t == None:
            return '\n'
        s = "-------------------------------------\n"
        for i in range(self.t.height+1):
            s += self.t.level(i) + '\n'
            
        s += "-------------------------------------" + '\n'
        return s
#------------------------------------------------------------

if __name__ == "__main__":
    bt = AVLTree()
    while True:
        c = 'a'
        print(bt)
        while(c not in 'iIdDfFeE'):
            c=input("Enter choice: (i)nsert, (d)elete, (f)ind, (e)xit:")
            c = c.rstrip()
        if c in 'iI':
            n = input("Enter integer to insert:")
            try:
                bt.insert(int(n))
            except ValueError:
                print ("BST insertion error")
        elif c in 'dD':
            n = input("Enter integer to delete:")
            try:
                bt.delete(int(n))
            except ValueError:
                print ("BST deletion error")
        elif c in 'fF':
            n = input("Enter integer to find:")
            try:
                bt.find(int(n))
            except ValueError:
                print ("BST find error")
        else:
            break
