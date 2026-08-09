'''
Oh no! Your flight has been cancelled and you need to rebook. 
Given an adjacency matrix of today's flights flights where each flight 
is labeled 0 to n-1 and flights[i][j] = 1 indicates that there is an 
available flight from location i to location j, return True if there 
exists a path from your current location source to your final destination 
dest. Otherwise return False.

Evaluate the time complexity of your function. 
Define your variables and provide a rationale for why you believe your 
solution has the stated time complexity.
'''

def dfs_iterative(grid, start_r, start_c):
  rows, cols = len(grid), len(grid[0])
  stack = [(start_r, start_c)]     # SLOT 1: seed -- same as recursive entry point

  while stack:
    r, c = stack.pop()

    # bounds + visited check here, not before pushing
    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
      continue            # SLOT 2: invalid cell -- same condition as base case

    grid[r][c] = '0'         # SLOT 3: mark visited -- same as recursive version

    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]: # SLOT 4: directions -- same
      stack.append((r+dr, c+dc))
'''
(DFS)
- Initialize an empty stack
- Initialize an empty list to store visited nodes
- Add the node we would like to start our traversal from to the stack
- while the stack is not empty:
    - Pop the topmost node off the stack and store it in a variable, `current`
    - If the node is not already in the list of visited nodes:
        - Add `current` to the list of visited nodes
    - Loop through the current node's neighbors:
        - If the neighbor has not yet been visited
            - Push the neighbor onto the stack
- Return list of visited nodes
'''
def dfs(grid, r, c, rows, cols):
 # BASE CASE -- change: OOB check + what counts as "invalid"
  if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
    return

  grid[r][c] = '0'     # MARK VISITED -- change: use visited set if can't mutate

  # RECURSE -- change: 4-dir vs 8-dir, or add return value (size, path, etc.)
  for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
    dfs(grid, r+dr, c+dc, rows, cols)

def can_rebook(flights, source, dest):
    rows, cols = len(flights), len(flights[0])
    visited_nodes = [(source, dest)]
    while visited_nodes:
        r, c = stack.pop()

        # bounds + visited check here, not before pushing
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            continue            # SLOT 2: invalid cell -- same condition as base case
        
        grid[r][c] = '0'         # SLOT 3: mark visited -- same as recursive version
        
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]: # SLOT 4: directions -- same
            stack.append((r+dr, c+dc))
    pass

flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2))

'''
Expected Output:
True
False
'''