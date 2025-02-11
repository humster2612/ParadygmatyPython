# Zad2
from collections import deque


def algbfs(graf, poczatek, koniec):
    queue = deque(poczatek)

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == koniec:
            return path, len(path)
        else:
            for neighbor in graf.get(node, []):
                queue.append(list(path) + [neighbor])

graf = {

    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']

}


print(algbfs(graf, 'A', 'G'))
