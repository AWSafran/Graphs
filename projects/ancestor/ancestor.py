from util import Queue

def earliest_ancestor(ancestors, starting_node):
    ancestor_paths = {}

    graph = {}

    for relation in ancestors:
        if relation[1] not in graph:
            graph[relation[1]] = set()
        # We want to make sure the parent is in there too, even if it doesn't have parents
        if relation[0] not in graph:
            graph[relation[0]] = set()
        
        graph[relation[1]].add(relation[0])

    # If starting node has no parents, return -1
    if graph[starting_node] == set():
        return -1

    q = Queue()

    visited = []

    q.enqueue(starting_node)
    ancestor_paths[starting_node] = [starting_node]

    max_path = 0
    max_ancestor = None

    while q.size() > 0:
        current = q.queue[0]
        visited.append(current)
        for parent in graph[current]:
            if parent not in visited:
                ancestor_paths[parent] = ancestor_paths[current] + [parent]
                q.enqueue(parent)
                if len(ancestor_paths[parent]) > max_path:
                    max_path = len(ancestor_paths[parent])
                    max_ancestor = parent
                if len(ancestor_paths[parent]) == max_path and parent < max_ancestor:
                    max_ancestor = parent

        q.dequeue()
    
    return max_ancestor

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 4)
