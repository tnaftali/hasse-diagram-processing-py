from Link import Link
from Node import Node
import hasse
import input_data

max_width = 1300
max_height = 700

def setup():
    size(1400, 800)


def draw():
    raw_data = input_data.get_data()
    data = hasse.optimize_data(raw_data)
    quadrants = hasse.get_quadrants(data, max_height)
    nodes = hasse.add_nodes(data, quadrants, max_width)
    hasse.add_links(data, nodes)
    noLoop()


setup()