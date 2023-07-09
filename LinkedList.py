from Node import Node

class LinkedList:
    
    def __init__(self, head_node_value):
        self.head = Node(head_node_value)

    def __repr__(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(current_node.value)
            current_node = current_node.right
        return f'<LinkedList: {" -> ".join(nodes)}>'
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.right

    def append_node(self, value):
        new_node = Node(value)
        for node in self:
            pass
        node.right = new_node
        # current_node = self.head
        # while current_node.right:
        #     current_node = current_node.right
        # current_node.right = new_node
        
    def insert_node(self, value, prev_node_value):
        new_node = Node(value) #we want to add a new item to the list
        for node in self:
            if node.value == prev_node_value:
                new_node.right = node.right
                node.right = new_node
                return 
        print(f'{prev_node_value = } not valid')

    def remove_node(self, value):
        if value == self.head.value:
            self.head = self.head.right
        else:
            for node in self:
                if node.right and node.right.value == value:
                    node.right = node.right.right
                    return
            print(f'Value: {value} not found')

    def remove_tail(self): #go through our linked list and remove the last item
        for node in self:
                pass
        self.remove_node(node.value)

    
    def get_tail(self): #return or print the last node in our linked list
        current_node = self.head
        while current_node.right:
            current_node = current_node.right
        return current_node
    
    def print_list(self): #output every node in our linked list
        for node in self:
            print(node.value, end=" ")
    
linked_list = LinkedList('monday')
linked_list.append_node('tuesday')
linked_list.append_node('wednesday')
linked_list.append_node('friday')

# print(linked_list)

# linked_list.insert_node('thurday', 'wednesday')
# linked_list.insert_node('sunday', 'saturday')

# needs __iter__ method
# for n in linked_list:
#     print(n)

# linked_list.remove_node('saturday')

print_ls = linked_list.print_list()
print(print_ls)
tail_node = linked_list.get_tail()
print(tail_node.value)

remove_out_node = linked_list.remove_tail()
print(remove_out_node)
# print([node for node in linked_list])