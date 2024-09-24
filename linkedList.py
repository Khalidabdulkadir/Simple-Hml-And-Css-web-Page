class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinledList:
    def __init__(self):
        self.head = None

    def insert_at_beggining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def Display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements

linked_list = LinledList()

linked_list.insert_at_beggining(10)
linked_list.insert_at_beggining(20)
linked_list.insert_at_beggining(40)
linked_list.insert_at_beggining(90)

print(linked_list.Display())
        