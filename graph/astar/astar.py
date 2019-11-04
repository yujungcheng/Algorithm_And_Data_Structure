#!/usr/bin/env python3
import sys
import copy

from maze import mazes
from node import Node
from common import *


SPACE = 0
BLOCK = 1

PRINT_MAZE = False
PRINT_PATH = True
PRINT_STEP = False
PRINT_MOVE = True
PRINT_COLOUR = True

NEIGHBOR_ORDER_MODE = 0


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

    # dump maze for discovery map (opened node map)
    open_map = copy.deepcopy(maze)
    # opened node list
    open_nodes = []
    # closed node list
    closed_nodes = []

    start_node = Node(parent=None, position=start_position)
    end_node = Node(None, position=end_position)

    open_nodes.append(start_node)

    lowest_cost = True

    move = 0
    while len(open_nodes) > 0:

        current_node, current_index = get_lowerest_cost_node(open_nodes, lowest_cost=lowest_cost)
        open_nodes.pop(current_index)
        closed_nodes.append(current_node)
        current_node.move = move

        # update discovery map by current node
        if PRINT_MOVE:
            x = current_node.position[0]
            y = current_node.position[1]
            if maze[x][y] != BLOCK:
                open_map[x][y] = 2
            print("Move %s" % move)
            print_discovery_map(open_map, colour=PRINT_COLOUR)
        move += 1

        # reached end node
        if current_node == end_node:
            break

        # check neighbor nodes of current node
        temp_neighbors = []
        neighbor_positions = current_node.get_neighbor_positions(order=NEIGHBOR_ORDER_MODE)

        for neighbor_position in neighbor_positions:

            if neighbor_position[1] > max_x or neighbor_position[0] > max_y:    # hit boundary
                continue
            if maze[neighbor_position[0]][neighbor_position[1]] != SPACE:   # hit barrier
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
            temp_neighbors.append(neighbor_node)

        lowest_cost = False
        for index, neighbor in enumerate(temp_neighbors):
            if neighbor.distance_to_end < current_node.distance_to_end:
                lowest_cost_neighbor = neighbor
                lowest_cost = True

    path = reconstruct_path(current_node)

    if PRINT_MAZE:
        print_maze_path(maze, start_position, end_position, color=PRINT_COLOUR)
    if PRINT_PATH:
        print_maze_path(maze, start_position, end_position, path=path, colour=PRINT_COLOUR)
    if PRINT_STEP:
        print_path(path)

    print("Maze Name : %s" % maze_name)
    print("- Steps in path => %s" % (len(path) - 1))
    print("- Open nodes => %s" % len(open_nodes))
    print("- Closed nodes => %s" % len(closed_nodes))
    print('')


if __name__ == '__main__':
    main()
