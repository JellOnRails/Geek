"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    return has_cycle_util(head, list())

def has_cycle_util(head, node_list):
    if head is None:
        return False

    node_list.append(head)
    
    if head.next in node_list:
        return True
    
    return has_cycle_util(head.next, node_list)