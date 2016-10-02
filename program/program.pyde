from Link import Link
from Node import Node
import hasse


max_width = 800
max_height = 600
raw_data = [
        [1, [2,3,4,5,6,10,12,15,20,30,60]],
        [2, [4,6,10,12,20,30,60]],
        [3, [6,12,15,30,60]],
        [4, [12,20,60]],
        [5, [10,15,20,30,60]],
        [6, [12,30,60]],
        [10, [20,30,60]],
        [12, [60]],
        [15, [30,60]],
        [20, [60]],
        [30, [60]],
        [60, []]
        ]


def setup():
    size(850, 600)

def keyTyped():
    if keyCode == UP:
        print 'a'

def draw():
    lines = loadStrings("data.txt")
    for line in lines:
        print(line)
    data = hasse.optimize_data(raw_data)
    quadrants = hasse.get_quadrants(data, max_height)
    nodes = hasse.add_nodes(data, quadrants, max_width)
    hasse.add_links(data, nodes)
    noLoop()


setup()