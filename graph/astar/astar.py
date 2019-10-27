#!/usr/bin/env python3
import sys

from maze import mazes
from node import Node
from common import *


SPACE = 0
BLOCK = 1

PRINT_MAZE = False
PRINT_PATH = True
PRINT_STEP = False


def main():

    if len(sys.argv) < 2:
        print("Missing maze name.")
        exit(1)

    maze_name = sys.argv[1]
    maze = mazes[maze_name]

    max_x = len(maze) - 1
    max_y = len(maze[max_x]) - 1

    start_position = (0, 0)
    end_position = (max_x, max_y)

    open_nodes = []
    closed_nodes = []

    start_node = Node(parent=None, position=start_position)
    end_node = Node(None, position=end_position)

    open_nodes.append(start_node)

    while len(open_nodes) > 0:

        current_node = open_nodes[0]
        #current_node = find_lowerest_cost_node(open_nodes)
        current_index = 0
        for index, item in enumerate(open_nodes):
            if item.cost < current_node.cost:
                current_node = item
                current_index = index

        open_nodes.pop(current_index)
        closed_nodes.append(current_node)

        # reached end node
        if current_node == end_node:
            break

        # check neighbor nodes of current node
        #neighbor_nodes = []
        neighbor_positions = current_node.get_neighbor_positions(order=None)
        for neighbor_position in neighbor_positions:
            x = neighbor_position[0]
            y = neighbor_position[1]

            if neighbor_position[1] > max_x or neighbor_position[0] > max_y:    # hit boundary
                continue
            if maze[x][y] != SPACE:   # hit barrier
            #if maze[neighbor_position[0]][neighbor_position[1]] != SPACE:   # hit barrier
                continue

            neighbor_node = Node(parent=current_node, position=neighbor_position)

            # skip closed node
            neighbor_in_closed_nodes = False
            for closed_node in closed_nodes:
                if neighbor_node == closed_node:
                    neighbor_in_closed_nodes = True
                    break
            if neighbor_in_closed_nodes:
                continue

            # calculate cost
            neighbor_node.distance_from_start = node_distance_from_start(current_node)
            neighbor_node.distance_to_end = node_distance_to_end(current_node, end_node)
            neighbor_node.cost = neighbor_node.distance_from_start + neighbor_node.distance_to_end

            # skip if neighbor node is in open nodes and has larger cost
            neighbor_in_open_nodes_larger_cost = False
            for open_node in open_nodes:
                if neighbor_node == open_node and neighbor_node.cost > open_node.cost:
                    neighbor_in_open_nodes_larger_cost = True
                    break
            if neighbor_in_open_nodes_larger_cost:
                continue

            open_nodes.append(neighbor_node)

        #print("%s %s" % (current_node, len(open_nodes)))

    path = reconstruct_path(current_node)

    print("Maze Name : %s" % maze_name)
    print("- Steps in path => %s" % (len(path) - 1))
    print("- Open nodes => %s" % len(open_nodes))
    print("- Closed nodes => %s" % len(closed_nodes))
    print('')

    if PRINT_MAZE:
        print_maze_path(maze, start_position, end_position)
    if PRINT_PATH:
        print_maze_path(maze, start_position, end_position, path=path)
    if PRINT_STEP:
        print_path(path)


if __name__ == '__main__':
    main()
