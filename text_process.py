class Node:
    def __init__(self):
        self.prev = 0
        self.sents = 0

node = Node()

def prev_node_state():
    return node

def process_data(data : list):

    for i in data:
        print(i)