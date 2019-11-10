#!/usr/bin/env python3
import time


def node_distance_from_start(current_node):
    return current_node.distance_from_start + 1

def node_distance_to_end(current_node, end_node):
    current_y = current_node.position[0]
    current_x = current_node.position[1]
    end_y = end_node.position[0]
    end_x = end_node.position[1]
    distance_y = (current_y - end_y) ** 2
    distance_x = (current_x - end_x) ** 2
    return distance_x + distance_y

def get_lowerest_cost_node(node_list, lowest='cost'):
    lowerest_node = node_list[0]
    lowerest_cost = node_list[0].cost
    lowerest_index = 0
    if lowest == 'move':
        return lowerest_node, 0
    elif  lowest == 'cost':
        # find lower cost node
        for index, node in enumerate(node_list):
            if node.cost < lowerest_node.cost:
                lowerest_node = node
                lowerest_index = index
    return lowerest_node, lowerest_index

def reconstruct_path(node):
    path = []
    current_node = node
    while current_node is not None:
        path.append(current_node.position)
        current_node = current_node.parent
    return path[::-1]

def print_maze_path(maze, start, end, path=None, colour=False, space=0, block=1):
    if path == None:
        print("[ Maze ]")
    else:
        print("[ Maze with path to end ]")
    print('-'*30)
    x = 0
    y = 0
    if path == None:
        path = [start, end]
    for row in maze:    # y
        for column in row:  # x
            if (x, y) in path:
                if (x, y) == start:
                    print("S ", end = '')
                elif (x, y) == end:
                    print("E ", end = '')
                else:
                    if colour:
                        print('\x1b[0;32;40m'+'M'+'\x1b[0m ', end = '')
                    else:
                        print("M ", end = '')
            else:
                if column == space:
                    print('. ', end = '')
                elif column == block:
                    if colour:
                        print('\x1b[0;31;40m'+'#'+'\x1b[0m ', end = '')
                    else:
                        print('# ', end = '')
            y += 1
        print('')
        y = 0
        x += 1
    print('')

def print_discovery_map(map, colour=False, delay=0.1):
    for i in map:
        for j in i:
            if j == 0:
                print(". ", end = '')
            elif j == 1:
                if colour:
                    print('\x1b[0;31;40m'+'#'+'\x1b[0m ', end = '')
                else:
                    print("# ", end = '')
            elif j == 2:
                if colour:
                    print('\x1b[0;32;40m'+'o'+'\x1b[0m ', end = '')
                else:
                    print("o ", end = '')
        print('')
    print('')
    time.sleep(delay)

def print_path(path, line=False):
    count = len(path)
    counter = 0
    for step in path:
        if line:
            print(step, end = ' > ')
        else:
            print("%3d > %s" % (counter, step))
            counter += 1
    print('')

def heuristic():
    return
