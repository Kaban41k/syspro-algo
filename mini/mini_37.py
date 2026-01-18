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
    def calculate_weights_and_nota(node):
        weights = []
        notas = []

        for i in node.children:
            weight, nota = calculate_weights_and_nota(i)

            weights.append(weight)
            notas.append(nota)

        weight = sum(weights) + 1

        nota = factorial(sum(weights))

        for n in weights:
            nota /= factorial(n)

        for nota_ch in notas:
            nota *= nota_ch

        return weight, nota

    root_weight, root_nota = calculate_weights_and_nota(root)
    return int(root_nota)


print(num_of_topsorted_arrays(root))