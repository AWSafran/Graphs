import random
from util import Queue
class User:
    def __init__(self, name):
        self.name = name
        self.id = None

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()
        self.users[self.lastID].id = self.lastID

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users

        for i in range(0, numUsers):
            self.addUser(str(i))

        # possible_friendships = []
        # for user in self.users:
        #     for friend in range(user + 1, self.lastID + 1):
        #         possible_friendships.append((user, friend))


        # selected_friendships = random.sample(possible_friendships, (numUsers * avgFriendships) // 2)

        #Our User ID starts at 1, not 0
        for i in range(1, numUsers):
            # randomly assign friends - number is random that should average to avgFriendships
            num_friends = random.randint(0, 2 * avgFriendships)
            friend_count = len(self.friendships[i])
            failed_friendships = 0
            while friend_count < num_friends:
                
                #modified addFriendships to return false if invalid friendship
                #Only indrement friend counter if we created a valid friendship
                if self.addFriendship(i, random.randint(i, numUsers)):
                    friend_count += 1
                else:
                    failed_friendships += 1

                if failed_friendships > 5:
                    break


        # for friendship in selected_friendships:
        #     self.addFriendship(friendship[0], friendship[1])
        # Create friendships

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        q = Queue()

        q.enqueue(userID)

        visited[userID] = [userID]

        while q.size() > 0:
            for friendID in self.friendships[q.queue[0]]:
                if friendID not in visited:
                    visited[friendID] = visited[q.queue[0]] + [friendID]
                    q.enqueue(friendID)
            q.dequeue()
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
