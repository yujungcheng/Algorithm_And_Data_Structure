#!/usr/bin/env python3

def node_distance_from_start(current_node):
    return current_node.distance_from_start + 1

def node_distance_to_end(current_node, end_node):
    current_x = current_node.position[0]
    current_y = current_node.position[1]
    end_x = end_node.position[0]
    end_y = end_node.position[1]
    distance_x = (current_x - end_x) ** 2
    distance_y = (current_y - end_y) ** 2
    return distance_x + distance_y

def reconstruct_path(node):
    path = []
    current_node = node
    while current_node is not None:
        path.append(current_node.position)
        current_node = current_node.parent
    return path[::-1]

def print_maze_path(maze, start, end, path=None, space=0, black=1):
    if path == None:
        print("[ Maze ]")
    else:
        print("[ Maze with path to end ]")
    print('-'*30)
    i = 0
    j = 0
    if path == None:
        path = [start, end]
    for row in maze:
        for column in row:
            if (i, j) in path:
                if (i, j) == start:
                    print("S ", end = '')
                elif (i, j) == end:
                    print("E ", end = '')
                else:
                    print("M ", end = '')
            else:
                if column == 0:
                    print('. ', end = '')
                elif column == 1:
                    print('# ', end = '')
            j += 1
        print('')
        j = 0
        i += 1
    print('')

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

def find_lowerest_cost_node(node_list):
    lowerest_node = node_list[0]
    lowerest_cost = node_list[0].cost
    for node in node_list:
        if node.cost < lowerest_cost:
            lowerest_node = node
    return lowerest_node
