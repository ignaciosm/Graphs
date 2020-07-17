from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue

# ******************************************** util **********************************


# *************************************** util ******************************************


# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# ***************************** SOLUTION BELOW **************************************
traversal_path = []
visited_rooms = set()

# graph = {
#     0: {'n': 1, 's': 5, 'w': 7, 'e': 3},
#     1: {'n': 2, 's': 0},
#     2: {'s': 1},
#     3: {'w': 0, 'e': 4},
#     4: {'w': 3},
#     5: {'n': 0, 's': 6},
#     6: {'n': 5},
#     7: {'w': 8, 'e': 0},
#     8: {'e': 7},
# }

# graph scaffold
graph = {}
for room in range(len(room_graph)):
    graph[room] = {}

back_directions = {
    'n': 's',
    's': 'n',
    'w': 'e',
    'e': 'w'
}

while len(visited_rooms) < len(room_graph):
    current_room = player.current_room.id
    if current_room not in visited_rooms:
        visited_rooms.add(player.current_room)

    # find exits
    exits = player.current_room.get_exits()

    # build graph
    if len(graph[current_room]) == 0:
        for exit in exits:
            graph[current_room][exit] = "?"

    # remove back from exits
    fwd_exits = exits[:]
    if len(traversal_path) > 0:
        back = back_directions[traversal_path[-1]]
        fwd_exits.remove(back)

    # select direction
    selected = random.choice(list(fwd_exits))
    print('moving', selected)

    new_room = player.current_room.get_room_in_direction(selected).id
    # print('current', current_room, 'new', new_room, back_directions[selected])
    graph[current_room][selected] = new_room
    graph[new_room][back_directions[selected]] = current_room
    # print('a', current_room, selected)
    # print('b', new_room, back_directions[selected])
    player.travel(selected)
    print(graph)
    # update graph
    # graph[selected][back] = old_room
    # print('graph', graph)

    traversal_path.append(selected)
    # print('traversal_path', traversal_path)


# ***************************** SOLUTION ABOVE **************************************


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
