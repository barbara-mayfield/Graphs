import random

"""
Functionality behind creating users and friendships has been completed already.

Implement a function that shows all the friends in a user's EXTENDED
social network and chain of friendships that link them.

Implement a feature that creates large #'s of users to the network &
assigns them a random distribution of friends.
"""

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0

        # maps user's ID to user objects 
        # (lookup table for user Objects given IDs)
        self.users = {}

        # Adjacency list
        # maps users to a list of other users
        # who are their friends 
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)

        # this is where we add our verts to our adjacency list
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # !!!! IMPLEMENT ME
        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        # Create friendships
        # Generate all possible friendships
        possible_friendships =  []    #[ (Friend_id_1, friend_id_2 )  ]
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append( (user_id, friend_id) )
        
        # randomize the above array
        random.shuffle(possible_friendships)

        # Pick out num_users * avg_friendships number of friend combos from possible_friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
            


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.

        What kind of graph search guarantees you the shortest path?

        Instead of using a set you could use a dict.
        If the visited user is the key, what would be the value?
        
        Visit every vertex and store the path to them
        
        Say we search through ID 1, we would
        want to go through and hit up every
        single connected user.

        If we use a BST we can accomplish that
        as we visit a node we want to retain the
        path to it, so instead of just simpy adding
        to the visited set (current id)

        Key would be the ID and the value would be the path
        """
        # !!!! IMPLEMENT ME
        # Create a Queue
        queue = Queue()
        # Create a dict of visited (previously seen vertices)
        visited = {}  # Note that this is a dictionary, not a set
        # Add first user_id to the Queue as a path
        queue.enqueue([user_id])

        # While the queue is not empty:
        while queue.size() > 0:
            # Dequeue current path
            current_path = queue.dequeue()
            # Get the current vertex from the end of path
            current_vertex = current_path[-1]
            # If current vertex NOT in visited set:
            if current_vertex not in visited:
                # add vertex to visited set
                # also add the path that brought us to this vertex
                # i.e.: add a key and value to the visited dict
                #   the key is the current vertex, and the value is the path
                visited[current_vertex] = current_path
                
                # queue up all neighbors to path
                for neighbor in self.friendships[current_vertex]:
                    # make a new copy of cur path
                    new_path = current_path.copy()
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(5, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
