import random

graph = {
    0: {'n': 1, 's': 5, 'w': 7, 'e': 3},
    1: {'n': 2, 's': 0},
    2: {'s': 1},
    3: {'w': 0, 'e': 4},
    4: {'w': 3},
    5: {'n': 0, 's': 6},
    6: {'n': 5},
    7: {'w': 8, 'e': 0},
    8: {'e': 7},
}

selected = 5

for key, value in graph[0].items():
    if value == selected:
        print('key', key)
