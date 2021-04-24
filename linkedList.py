class node:
	def __init__(self, data = None) -> None:
		self.data = data
		self.next = None
class linkedList:
	def __init__(self) -> None:
		self.head = node()

	def append(self, data):
		newNode = node(data)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = newNode

	def length(self):
		cur = self.head
		total = 0
		while cur.next != None:
			total += 1
			cur = cur.next
		return total

	def display(self):
		elem = []
		cur = self.head
		while cur.next != None:
			cur = cur.next
			elem.append(cur.data)
		print(elem)
		
myLinkedList = linkedList()
myLinkedList.display()
myLinkedList.append('2')
myLinkedList.append('f')
myLinkedList.display()
