# returns their earliest known ancestor – the one at the farthest distance from the input individual

# ancestors = [
#     (1, 3),
#     (2, 3),
#     (3, 6),
#     (5, 6),
#     (5, 7),
#     (4, 5),
#     (4, 8),
#     (8, 9),
#     (11, 8),
#     (10, 1)
# ]

# starting_node = 6


def earliest_ancestor(ancestors, starting_node):
    queue = []
    queue.append(starting_node)
    visited = set()
    while len(queue) > 0:
        current = queue.pop()
        visited.add(current)
        for ancestor in ancestors:
            if ancestor[1] == current:
                queue.append(ancestor[0])
    if current == starting_node:
        return -1
    else:
        return current
