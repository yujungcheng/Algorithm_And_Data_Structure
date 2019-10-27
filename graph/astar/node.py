#!/usr/bin/env python3


class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent    # parent node
        self.position = position    # (x, y)
        self.cost = 0
        self.distance_from_start = 0
        self.distance_to_end = 0

    def __str__(self):
        if self.position == None:
            return "None"
        else:
            return str(self.position)

    def __eq__(self, node):
        return self.position == node.position

    def is_position(self, x, y):
        if self.position[0] == x and self.position[1] == y:
            return True
        return False

    def get_neighbor_positions(self, order=None):
        neighbors = []
        offsets = []
        if order == 0:
            offsets = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        elif order == 1:
            offsets = [(1,-1),(1,0),(0,-1),(1,1),(-1,-1),(0,1),(-1,0),(-1,1)]
        elif order == 2:
            offsets = [(1,-1),(1,0),(0,-1),(1,1),(-1,-1),(0,1),(-1,0),(-1,1)]
        elif order == 3:
            offsets = [(0,1),(0,-1),(-1,0),(1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
        elif order == 4:
            offsets = [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
        else:
            for x_offset in [-1, 1, 0]:
                for y_offset in [-1, 1, 0]:
                    if x_offset == 0 and y_offset == 0:
                        continue
                    offsets.append((x_offset, y_offset))
        #print(offsets)
        for offset in offsets:
            x = self.position[0] + offset[0]
            y = self.position[1] + offset[1]
            if x < 0 or y < 0:
                continue
            neighbors.append((x,y))
        return neighbors[1:]
