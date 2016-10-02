import random


class Node(object):
    def __init__(self, number, subnodes, max_width, min_height, max_height):
        self.subnodes = subnodes
        self.x = random.randint(20, max_width - 20)
        self.y = random.randint(min_height, max_height)
        self.number = str(number)
        fill(255)
        ellipse(self.x, self.y, 20, 20)
        fill(0,0,0)
        textSize(18)
        text(self.number, self.x - 5, self.y + 30)