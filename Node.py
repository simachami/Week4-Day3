class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


    def __repr__(self):
        return f'<Node: {self.value}>'

node = Node('monday')

if __name__ == '__main__':
    print(node)

#'monday' -> 'tuesday' -> 'wednesday' -> 'friday'




