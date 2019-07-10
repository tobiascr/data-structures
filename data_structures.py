"""A module that consists of various implementations of data structures that
can be used for solving programming exercises.
"""

import random


class Stack():
    def __init__(self):
        self.list = []
    def push(self, element):
        self.list.append(element)
    def pop(self):
        return list.pop(self.list)


class Queue():
    def __init__(self):
        self.list = []
    def enqueue(self, element):
        self.list.insert(0, element)
    def dequeue(self):
        return list.pop(self.list)


class SinglyLinkedList:
    """A node that can be used to make a singly linked list."""
    def __init__(self, *values):
        self.value = None                
        self.next_node = None

        node = self
        is_first = True
        for v in values:
            if is_first:
                self.value = v
                is_first = False
            else:
                new_node = SinglyLinkedList()
                new_node.value = v                
                node.next_node = new_node
                node = new_node
        
    def __str__(self):
        """Make it possible to use the print command on objects of this class."""
        output = ""
        node = self        
        while node:
            output += str(node.value)
            node = node.next_node
            if node:
                output += " -> "
        return output


class Node:
    """A node that can be used to make a tree."""
    def __init__(self, value=None):
        self.value = value
        self.children = []
        
        
class BinaryNode:
    """A node that can be used to make a binary tree."""
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        """Make it possible to use the print command on objects of this class."""
                
        def character_block(tree, title="Root"):
            """Return a list of strings that corresponds to the rows of the tree."""                
            rows = [title + ": " + str(tree.value)]                                                                                                                                                                      
            if tree.left_child and tree.right_child:
                block = character_block(tree.left_child, title = "L")
                rows.append(" ├── " + block[0])                   
                for i in range(1, len(block)):
                    rows.append(" │   " + block[i])
                block = character_block(tree.right_child, title = "R")
                rows.append(" └── " + block[0])
                for i in range(1, len(block)):
                    rows.append("     " + block[i])
            elif tree.left_child:
                block = character_block(tree.left_child, title = "L")
                rows.append(" └── " + block[0])
                for i in range(1, len(block)):
                    rows.append("     " + block[i])
            elif tree.right_child:
                block = character_block(tree.right_child, title = "R")
                rows.append(" └── " + block[0])
                for i in range(1, len(block)):
                    rows.append("     " + block[i])                                
            return rows
                   
        return "\n".join(character_block(self))
        
        
def print_tree(tree, steps_of_indentation=0):
    spaces = "  " * steps_of_indentation
    print(spaces + str(tree.value))
    for child in tree.children:
        print_tree(child, steps_of_indentation + 1)

def random_tree(max_height=4, max_children_per_node=4):
    """Return a random tree with integer node values."""
    tree = Node(random.randrange(10))
    
    if max_height > 0:
        number_of_children = random.randrange(0, max_children_per_node + 1)
        for n in range(0, number_of_children):
            child = random_tree(max_height - 1, max_children_per_node)
            #tree.add_child(child)
            tree.children.append(child)                
    return tree
    
def random_binary_tree(value_list):
    """Return a random binary tree with the values in value_list.
    Each entry in the list occurs exactly one time.
    """
    # The root of the tree is created.
    value = random.choice(value_list)
    value_list.remove(value)        
    root = BinaryNode(value)
            
    # A list with nodes that don't have both a left and a right child.    
    available_nodes = [root]
    
    while value_list:
        # Make a new node
        value = random.choice(value_list)
        value_list.remove(value)
        new_child = BinaryNode(value)
                
        # Add the node to the tree.
        random_node = random.choice(available_nodes)
        if random_node.left_child:
            random_node.right_child = new_child
            available_nodes.remove(random_node)
        elif random_node.right_child:
            random_node.left_child = new_child
            available_nodes.remove(random_node)
        elif random.randrange(2) == 0:
            random_node.left_child = new_child
        else:
            random_node.right_child = new_child        
        
        available_nodes.append(new_child)
        
    return root

def random_binary_search_tree(values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]):
    """Return a randomly arranged binary search trees that have the node values
    in values.
    """
    root_value = random.choice(values)
    values.remove(root_value)
    
    binary_search_tree = BinaryNode(root_value)
    
    left_values = []
    right_values = []
    
    for value in values:
        if value < root_value:
            left_values.append(value)
        if value > root_value:
            right_values.append(value)
        if value == root_value:
            if random.randrange(2) == 0:
                left_values.append(value)
            else:
                right_values.append(value)
    
    if left_values:
        binary_search_tree.left_child = random_binary_search_tree(left_values)
    if right_values:
        binary_search_tree.right_child = random_binary_search_tree(right_values)
        
    return binary_search_tree

def height(binary_tree):

    if not binary_tree.left_child and not binary_tree.right_child:    
        return 0                
    else:            
    
        if binary_tree.left_child:
            left_height = height(binary_tree.left_child)
        else:
            left_height = 0
            
        if binary_tree.right_child:
            right_height = height(binary_tree.right_child)
        else:
            right_height = 0
                
        return max(left_height + 1, right_height + 1)
        
def is_end_node(binary_tree_node):
    if not binary_tree_node.left_child and not binary_tree_node.right_child:
        return True
    else:
        return False    

def random_end_node(binary_tree):
    """Return a random end node of binary_tree."""
    if is_end_node(binary_tree):
        return binary_tree
    elif not binary_tree.left_child:
        return random_end_node(binary_tree.right_child)
    elif not binary_tree.right_child:
        return random_end_node(binary_tree.left_child)
    elif random.randrange(2) == 0:
        return random_end_node(binary_tree.left_child)
    else:    
        return random_end_node(binary_tree.right_child)         
