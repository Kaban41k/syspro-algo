from math import factorial


class Node:
    def __init__(self, id=None):
        self.children = []
        self.id = id


root = Node(0)
nodes = [root]
nodes_n = 1


def add_node(parent, node):
    global nodes
    global nodes_n

    parent.children.append(node)
    nodes.append(node)
    nodes_n += 1


add_node(root, Node(1))
add_node(root, Node(2))
add_node(root, Node(3))
add_node(nodes[1], Node(4))
add_node(nodes[2], Node(5))


def num_of_topsorted_arrays(root):
    weights = []

    def calculate_weights(node):
        weight = 1

        for i in node.children:
            weight += calculate_weights(i)

        weights.append(weight)
        return weight

    root_weight = calculate_weights(root)

    result = factorial(root_weight)
    for weight in weights:
        result //= weight

    return result


print(num_of_topsorted_arrays(root))