"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import collections


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Create the new key with the vertex ID, and set the value to an empty set (meaning no edges yet)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Find vertex V1 in our vertices, add V2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting_vertex

        queue = Queue()
        queue.enqueue(starting_vertex)

        # Create an empty set to track visited vertices
        visited = set()

        # While the queue is not empty:
        while queue.size() > 0:
            # Get current vertex (dequeue from queue)
            current_vertex = queue.dequeue()
            # Check if the current vertex has not been visited:
            if current_vertex not in visited:
                # Print the current vert
                print(f"{current_vertex}")
                # Mark the current vert as visited
                # Add the current vertex to a visited_set
                visited.add(current_vertex)
                neighbors = self.get_neighbors(current_vertex)
            # Queue up all the current vertex's neighbors (so we can visit them next)
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and add the starting_vertex
        stack = Stack()
        stack.push(starting_vertex)
        # Create an empty set to track visited verticies
        visited = set()
        # while the stack is not empty:
        while stack.size() > 0:
            # get current vertex (pop from stack)
            current_vertex = stack.pop()
            # Check if the current vertex has not been visited:
            if current_vertex not in visited:
                # print the current vertex
                print(f"{current_vertex}")
                # Mark the current vertex as visited
                # Add the current vertex to a visited_set
                visited.add(current_vertex)

                # push up all the current vertex's neighbors (so we can visit them next)
                neighbors = self.get_neighbors(current_vertex)

                for neighbor in neighbors:
                    if neighbor not in visited:
                        stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # We need to keep track of visited vertices outside of the
        # recursive call and mark the vertices as visited
        visited.add(starting_vertex)
        print(f"DFT_R: {starting_vertex}")

        # For each neighbor
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            # if it's not visited recurse on the neighbor
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue the PATH TO starting_vertex
        queue = Queue()
        path = [starting_vertex]
        queue.enqueue(path)
        # Create an empty set to track visited verticies
        visited = set()

        # while the queue is not empty:
        while queue.size() > 0:
            # get current vertex PATH (dequeue from queue)
            current_path = queue.dequeue()
            # set the current vertex to the LAST element of the PATH
            current_vertex = current_path[-1]

            # Check if the current vertex has not been visited:
            if current_vertex not in visited:
                # CHECK IF THE CURRENT VERTEX IS DESTINATION
                if current_vertex == destination_vertex:
                    # IF IT IS, STOP AND RETURN
                    return current_path

                # Mark the current vertex as visited
                # Add the current vertex to a visited_set
                visited.add(current_vertex)

                # Queue up NEW paths with each neighbor:
                neighbors = self.get_neighbors(current_vertex)

                for neighbor in neighbors:
                    # take current path
                    path_copy = current_path[:]
                    # append the neighbor to it
                    path_copy.append(neighbor)
                    # queue up NEW path
                    queue.enqueue(current_path + [neighbor])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push starting_vertex
        stack = Stack()
        stack.push(starting_vertex)

        # Create an empty set to hold visited vertices
        visited = set()

        # While the stack is not empty:
        while stack.size() > 0:
            # Get current vertices and add to visited set
            current_vertices = stack.pop()
            visited.add(current_vertices)

            neighbors = self.get_neighbors(current_vertices)
            # For each neighbor
            for neighbor in neighbors:
                # If it hasn't been visited push
                if neighbor not in visited:
                    stack.push(neighbor)
                # If the edge is the destination_vertex
                if neighbor is destination_vertex:
                    # Add edge to visited and return a list of visited path
                    visited.add(neighbor)
                    return list(visited)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        # If there are no visited vertices
        if visited is None:
            # Create an empty set
            visited = set()
            # Our path will be set to a deque list
            path = collections.deque([])
            # Add the starting vert to the path
            path.append([starting_vertex])

        # Mark vertices as visited and add to the set
        visited.add(starting_vertex)
        # Remove the current vertices from the path
        current_vertices = path.pop()
        # Track the last vertices
        last_vertices = current_vertices[-1]

        neighbors = self.get_neighbors(last_vertices)

        # For each last vertices in neighbors
        for last_vertices in neighbors:
            # If it isn't visited
            if last_vertices not in visited:
                # Create a new list to keep track of our route
                route = list(current_vertices)
                # Add the last vertices to the route
                route.append(last_vertices)
                # Add the route to the path
                path.append(route)

                if last_vertices is destination_vertex:
                    return route
        return self.dfs_recursive(last_vertices, destination_vertex, visited, path)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
