import random


class Node(object):
    def __init__(self, number, subnodes, max_width, min_height, max_height):
        self.subnodes = subnodes
        self.x = random.randint(20, max_width - 20)
        self.y = random.randint(min_height, max_height)
        self.number = str(number)
        fill(0)
        ellipse(self.x, self.y, 10, 10)
        textSize(14)
        text(self.number, self.x - 5, self.y + 30)