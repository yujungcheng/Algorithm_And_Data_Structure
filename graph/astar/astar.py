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

# neighbor
NEIGHBOR_ORDER_MODE = None

# set to None, 'cost' or 'move'
SET_LOWEST_TYPE = None


def main():

    if len(sys.argv) < 2:
        print("Missing maze name.")
        exit(1)

    maze_name = sys.argv[1]
    maze = mazes[maze_name]

    max_y = len(maze) - 1
    max_x = len(maze[max_y]) - 1

    start_position = (0, 0)
    end_position = (max_y, max_x)

    open_map = copy.deepcopy(maze) # dump maze for discovery map (opened node map)
    discovery_map = copy.deepcopy(maze)
    open_nodes = []  # store nodes to be opened
    closed_nodes = []  # store nodes that have been opened

    start_node = Node(parent=None, position=start_position)
    end_node = Node(None, position=end_position)

    open_nodes.append(start_node)

    # lowest type for pickup next node, 'cost' or 'move'.
    # use cost in beginning.
    lowest = 'cost'
    # move count for node
    move = 0

    while len(open_nodes) > 0:

        if SET_LOWEST_TYPE != None:
            lowest = SET_LOWEST_TYPE

        # get node from open node list
        current_node, current_index = get_lowerest_cost_node(open_nodes, lowest=lowest)
        open_nodes.pop(current_index)
        closed_nodes.append(current_node)
        current_node.move = move

        # update discovery map by current node
        if PRINT_MOVE:
            y = current_node.position[0]
            x = current_node.position[1]
            if maze[y][x] != BLOCK:
                open_map[y][x] = 2
            print("Move %s" % move)
            print_discovery_map(open_map, colour=PRINT_COLOUR)

        move += 1

        # reached end node
        if current_node == end_node:
            break

         # set to 'move' here,
         # will set to 'cost' when neighbors met condition,
        lowest = 'move'

        # check neighbor nodes of current node
        neighbor_positions = current_node.get_neighbor_positions(order=NEIGHBOR_ORDER_MODE)
        for neighbor_position in neighbor_positions:

            if neighbor_position[0] > max_x or neighbor_position[1] > max_y:    # hit boundary
                continue
            if discovery_map[neighbor_position[0]][neighbor_position[1]] != SPACE:   # hit barrier
                continue

            neighbor_node = Node(parent=current_node, position=neighbor_position)
            neighbor_node.move = move

            # if neighbor node is in closed node, skip it
            neighbor_in_closed_nodes = False
            for closed_node in closed_nodes:
                if neighbor_node == closed_node:
                    neighbor_in_closed_nodes = True
                    break
            if neighbor_in_closed_nodes:
                continue

            # calculate cost
            neighbor_node.distance_from_start = node_distance_from_start(current_node)
            neighbor_node.distance_to_end = node_distance_to_end(neighbor_node, end_node)
            neighbor_node.cost = neighbor_node.distance_from_start + neighbor_node.distance_to_end

            # skip if neighbor node is in open nodes and has larger cost
            neighbor_in_open_nodes_larger_cost = False
            for open_node in open_nodes:
                if neighbor_node == open_node and neighbor_node.cost > open_node.cost:
                    neighbor_in_open_nodes_larger_cost = True
                    break
            if neighbor_in_open_nodes_larger_cost:
                continue

            # append neighbor to open nodes
            open_nodes.append(neighbor_node)

            discovery_map[neighbor_position[0]][neighbor_position[1]] = 2

            # if find a neighbor is closer to end node, keep use 'cost'
            if neighbor_node.distance_to_end < current_node.distance_to_end:
                lowest = 'cost'

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
