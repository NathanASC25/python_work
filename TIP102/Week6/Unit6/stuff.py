'''
Given the head of a linked list playlist, return a dictionary that maps each artist in the list to its frequency.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

'''
# U - Understand the problem - 
         # I: Inputs - linked list
         # O: Outputs - dictionary
         # C: Constraints - frequency of artist, integer (number of repeats)
         # E: Edge Cases -empty list

#M - Match (have you seen this problem before?) - frequency map

# P - Plan your approach (written plan or pseudo code)

'''

'''
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
    freq = {}
    head = playlist
    
    if head is None:
        return {}
    
    while head:
        # Should there be a key
        #freq.artist = 
        freq[head.artist] = freq.get(head.artist, 0) +1
        head = head.next
    return freq


playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))
'''

'''
{ "SZA": 2, "Jimin" : 1, "Sabrina Carpenter": 1}
'''


# Problem 3

'''
The following code attempts to remove the first node with a given song from a singly linked list with head playlist_head but it contains a bug!

Step 1: Copy this code into your IDE.

Step 2: Create your own test cases to run the code against, and use print statements and the stack trace to identify and fix the bug so that the function 
correctly removes a node by value from the list.

Step 3: Evaluate the time and space complexity of the fixed solution. 
Define your variables and provide a rationale for why you believe the solution has the stated time and space complexity.

'''
'''
# U - Understand the problem - 
         # I: Inputs - linked list
         # O: Outputs - dictionary
         # C: Constraints - frequency of artist, integer (number of repeats)
         # E: Edge Cases -empty list

#M - Match (have you seen this problem before?) - frequency map

# P - Plan your approach (written plan or pseudo code)

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next
        
# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next  # Error
            return playlist_head 
        current = current.next

    return playlist_head


playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

# Expected Output: ('SOS', 'ABBA') -> ('Simple Twist of Fate', 'Bob Dylan') -> ('Lovely Day', 'Bill Withers')

print_linked_list(remove_song(playlist, "Dreams"))
'''

# Problem 4

'''
A variation of the two-pointer technique introduced in previous units is to have a slow and a fast pointer that increment at different rates.

We would like to check whether our playlist loops or not. Given the head of a linked list playlist_head, return True 
if the playlist has a cycle in it and False otherwise. A linked list has a cycle if at some point in the list, 
the node’s next pointer points back to a previous node in the list.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''
'''
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def on_repeat(playlist_head):
    slow = playlist_head
    fast = playlist_head
    if playlist_head is None:
        return False
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    return False

song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(on_repeat(song1))
'''

# Problem 5

'''
Given the head of a linked list playlist_head that may contain a cycle, use the fast and slow pointer method to return the length of the cycle. 
If the list does not contain a cycle, return 0.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has 
the stated time and space complexity.
'''

class SongNode:
    def __init__(self, song, artist, next=None)
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def loop_length(playlist_head):
    pass
