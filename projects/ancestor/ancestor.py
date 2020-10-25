
from util import Queue

# U - Understand
# Input will not be empty and there are no cycles.
# There are no repeated ancestors.
# IDs will always be positive integers.
# A parent can have any # of children.

# Input: (dataset, ID)  
# Output: oldest ancestor ID

def get_ancestor(ancestors, child):
    individuals = []
    for individual in ancestors:
        if individual[1] == child:
            individuals.append(individual[0])
    return individuals


def earliest_ancestor(ancestors, starting_node):
    # create empty queue
    queue = Queue()
    # add starting node to queue
    queue.enqueue([starting_node])
    # create set to store visited vertices
    visited = set()
    # initialize path length
    path_len = 1
    # oldest parent -1 if no parent
    oldest = -1

    #while size of q is greater than 0
    while queue.size() > 0:
        # dequeue first path
        path = queue.dequeue()
        #grab the last vertex from the path
        current_node = path[-1]

        #if that vertex has not been visited
        if current_node not in visited:
            #mark as visited
            visited.add(current_node)

        if len(path) >= path_len and current_node < oldest or len(path) > path_len:
            # updates path length
            path_len = len(path)
            # updates oldest parent
            oldest = current_node

        for parent in get_ancestor(ancestors, current_node):
            path_copy = list(path)
            path_copy.append(parent)
            queue.enqueue(path_copy)

    return oldest