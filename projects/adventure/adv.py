from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue

# ******************************************** util **********************************


# def find_shortest_path(current_room):
#     # initialize queue with the player in the first room
#     queue = Queue()
#     queue.enqueue([player.current_room.id])
#     visited = set()
#     while queue.size() > 0:
#         # start the path by dequeing the room
#         path = queue.dequeue()
#         current = path[-1]
#         # the room was now visited
#         if current not in visited:
#             visited.add(current)
#             # for room in next available rooms from current location:
#             for room in graph[current_room]:
#                 # if the room has not yet been traveled to
#                 if graph[current_room][selected] == "?":
#                     return path
#                 else:
#                     new_path = list(path)
#                     new_path.append(room_map[current][room])
#                     queue.enqueue(new_path)
#     return []


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
# traversal_path = []
# reverse_path = []
# visited_rooms = {}

# # visited_rooms = {
# #     0: {'n': 1, 's': 5, 'w': 7, 'e': 3},
# #     1: {'n': 2, 's': 0},
# #     2: {'s': 1},
# #     3: {'w': 0, 'e': 4},
# #     4: {'w': 3},
# #     5: {'n': 0, 's': 6},
# #     6: {'n': 5},
# #     7: {'w': 8, 'e': 0},
# #     8: {'e': 7},
# # }

# visited_rooms[player.current_room.id] = player.current_room.get_exits()

# # graph scaffold
# # graph = {}
# # for room in range(len(room_graph)):
# #     graph[room] = {}

# # unexplored = {}
# # for room in range(len(room_graph)):
# #     unexplored[room] = []

# back_directions = {
#     'n': 's',
#     's': 'n',
#     'w': 'e',
#     'e': 'w'
# }

# while len(visited_rooms) < len(room_graph):
#     current_room = player.current_room.id

#     # current room was not visited before
#     if current_room not in visited_rooms:


#         # add to our visited rooms set
#         # visited_rooms[current_room] = {}
#         # for exit in player.current_room.get_exits():
#         #     visited_rooms[current_room][exit] = "?"
#         # print('visited_rooms', visited_rooms)
#         # add to graph


#     # # find exits
#     # exits = player.current_room.get_exits()

#     # # build graph
#     # if len(graph[current_room]) == 0:
#     #     for exit in exits:
#     #         graph[current_room][exit] = "?"
#     #         unexplored[current_room] = exits

#     # # remove back from exits
#     # fwd_exits = exits[:]
#     # if len(traversal_path) > 0:
#     #     back = back_directions[traversal_path[-1]]
#     #     fwd_exits.remove(back)

#     # # select direction
#     # # unexplored = []
#     # # for key, value in graph[current_room].items():
#     # #     if value == "?":
#     # #         unexplored.append(key)

#     # if len(fwd_exits) > 0:
#     #     selected = random.choice(list(fwd_exits))
#     #     # unexplored[current_room].remove(selected)
#     #     print('x', unexplored[current_room])
#     # else:
#     #     # last = traversal_path[-1]
#     #     print('dead end')
#     #     selected = back
#     #     # print('fwd_exits', fwd_exits)
#     #     # player.travel(selected)
#     # new_room = player.current_room.get_room_in_direction(selected).id
#     # print('moving', selected, 'from', current_room, 'to', new_room)
#     # graph[current_room][selected] = new_room
#     # graph[new_room][back_directions[selected]] = current_room
#     # player.travel(selected)
#     # print('unexplored', unexplored)
#     # print('x', unexplored[current_room])
#     # # print(graph)
#     # # update graph
#     # # graph[selected][back] = old_room
#     # # print('graph', graph)

#     # traversal_path.append(selected)
#     # reverse_path.append(back_directions[selected])
#     # # print('traversal_path', traversal_path)


traversal_path = []
reverse_path = []
visited = {}

invert_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# Add initial room to visited dictionary, with exits as values
visited[player.current_room.id] = player.current_room.get_exits()
# visited {0: ['n', 's', 'w', 'e']}

# visited[player.current_room.id] = {}
# for exit in player.current_room.get_exits():
#     visited[player.current_room.id][exit] = "?"
# visited {0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}}

# print('visited', visited)

# MAIN LOOP
while len(visited) < len(room_graph) - 1:
    # if current room not in visited dict
    if player.current_room.id not in visited:
        # Add current room to visited dictionary, with exits as values
        visited[player.current_room.id] = player.current_room.get_exits()
        # Direction to go back
        go_back = reverse_path[-1]
        # Remove go back from visited exits in dict
        visited[player.current_room.id].remove(go_back)

    # WHILE IN A DEAD END
    while len(visited[player.current_room.id]) == 0:
        # while there are no unexplored rooms, go back untill unexplored rooms > 0
        reverse_direction = reverse_path.pop()
        traversal_path.append(reverse_direction)
        player.travel(reverse_direction)

    # Move forward towards the first unexplored room
    move_to = visited[player.current_room.id].pop(0)
    traversal_path.append(move_to)
    reverse_path.append(invert_direction[move_to])
    player.travel(move_to)

    # # CALCULATE EXITS
    # exits = player.current_room.get_exits()
    # fwd_exits = exits[:]
    # if len(traversal_path) > 0:
    #     back = invert_direction[traversal_path[-1]]
    #     fwd_exits.remove(back)

    # # print('fwd_exits', fwd_exits)
    # selected = random.choice(list(fwd_exits))
    # new_room = player.current_room.get_room_in_direction(selected).id

    # traversal_path.append(selected)
    # reverse_path.append(invert_direction[selected])
    # # print('traversal_path', traversal_path)
    # print('go', selected, 'from', player.current_room.id, 'to', new_room)
    # player.travel(selected)

# traversal_path = []
# reverse_path = []
# visited = {}
# unexplored = {}

# invert_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# # INITIAL NODE
# current_room = player.current_room.id
# exits = player.current_room.get_exits()
# unexplored[current_room] = exits

# # MAIN LOOP
# while len(visited) < len(room_graph) - 1:
#     # variables
#     current_room = player.current_room.id
#     exits = player.current_room.get_exits()
#     # unexplored[current_room] = exits
#     print('current_room', current_room)
#     # print('exits', exits)

#     # if current room not in visited:
#     if current_room not in visited:
#         visited[current_room] = {}
#         for e in exits:
#             visited[current_room][e] = "?"
#         unexplored[current_room] = exits
#     print('visited', visited)
#     print('unexplored', current_room, unexplored[current_room])

#     # WHILE IN A DEAD END
#     while len(unexplored[current_room]) == 0:
#         # print('reverse_path', reverse_path)
#         if len(reverse_path) > 0:
#             reverse_direction = reverse_path.pop(-1)
#             traversal_path.append(reverse_direction)
#             player.travel(reverse_direction)
#         else:
#             break

#     # MOVING FORWARD
#     # select direction
#     new_exits = unexplored[current_room]
#     if len(new_exits) > 0:
#         move_to = random.choice(list(new_exits))
#         print('move_to', move_to)
#     new_room = player.current_room.get_room_in_direction(move_to).id
#     print('new_room', new_room)

#     # update visited and unexplored
#     visited[current_room][move_to] = new_room
#     visited[new_room] = {}
#     visited[new_room][invert_direction[move_to]] = current_room
#     unexplored[current_room].remove(move_to)
#     unexplored[new_room] = player.current_room.get_room_in_direction(
#         move_to).get_exits()
#     unexplored[new_room].remove(invert_direction[move_to])
#     # print('unexplored curr', current_room, unexplored[current_room])
#     traversal_path.append(move_to)
#     reverse_path.append(invert_direction[move_to])
#     # print('reverse_path', reverse_path)

#     player.travel(move_to)


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
