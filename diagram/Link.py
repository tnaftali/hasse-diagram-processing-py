class Link(object):
    def __init__(self, x1, y1, x2, y2):
        strokeWeight = 10
        # stroke(random(0, 255), random(0, 255), random(0, 255));
        line(x1, y1, x2, y2)