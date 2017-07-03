class Node:
	def __init__(self, val)
	self.next = None
	self.data = val

def deleteDuplicates(head):

	if head.next == None:
		return head

	node = head
	t_node = node

	while node.next:

		while node.next:

			if node.data == t_node.next.data:
				t_node.next = t_node.next.next

			t_node = t_node.next

		node = node.next

	return head