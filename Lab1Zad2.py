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

    '1' : ['2','3','5'],
    '2' : ['1','4'],
    '3': ['1', '5', '6'],
    '4': ['2', '7'],
    '5': ['1', '3','7'],
    '6': ['3', '8'],
    '7': ['4', '5', '8'],
    '8': ['6', '7'],

}
print(algbfs(graf, '1', '4'))
