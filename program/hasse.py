from Node import Node
from Link import Link


def get_quadrants(data, max_height):
    quadrants = []
    quadrant_length = max_height / len(data)
    aux = 0
    for i in range(len(data)):
        quadrants.append([aux, aux + quadrant_length])
        aux += quadrant_length
    return quadrants


def add_node(nodes, num, subnodes, quadrants, quad_num, max_width):
    node = Node(num, subnodes, max_width, quadrants[quad_num][0], quadrants[quad_num][1])
    nodes.append(node)


def add_nodes(data, quadrants, max_width):
    nodes = []
    for i in range(len(data)):
        num = data[i][0]
        subnodes = data[i][1]
        add_node(nodes, num, subnodes, quadrants, (len(data) - 1) - i, max_width)
    return nodes


def add_links(data, nodes):
    for i in range(len(nodes)):
        node = nodes[i]
        for j in range(len(node.subnodes)):
            subnode_num = node.subnodes[j]
            subnode = search_node(subnode_num, nodes)
            if subnode != None:
                Link(node.x, node.y, subnode.x, subnode.y)


def search_node(num, nodes_list):
    found = False
    i = 0
    while not found and i < len(nodes_list):
        actual = nodes_list[i]
        if actual.number == str(num):
            found = True
            return actual
        i += 1
    return None


def optimize_data(data):
    for i in range(len(data)):
        subnodes_length = len(data[i][1])
        j = 0
        while j < subnodes_length:
            subnode = data[i][1][j]
            subnode_list = get_subnode_list(subnode, data)
            if subnode_list != None:
                for k in range(len(subnode_list)):
                    remove_node_from_subnodes(subnode_list[k], data[i][1])
                    subnodes_length -= 1
            j += 1
    return data
    

def get_subnode_list(node, data):
    found = False
    i = 0
    while not found and i < len(data):
        actual = data[i]
        if actual[0] == node:
            found = True
            return actual[1]
        i += 1
    return None


def remove_node_from_subnodes(node, subnodes):
    found = False
    i = 0
    while not found and i < len(subnodes):
        actual = subnodes[i]
        if actual == node:
            found = True
            del subnodes[i]
        i += 1