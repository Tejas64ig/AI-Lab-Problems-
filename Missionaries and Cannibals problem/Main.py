from collections import deque
M = 3  # Total Missionaries
C = 3  # TotalCannibals
boat_max = 2 #boar capacity

def safe_state(left_m, left_c): 
    right_m = M - left_m
    right_c = C - left_c
    return (left_m == 0 or left_m >= left_c) and (right_m == 0 or right_m >= right_c)

def show_state(lm, lc, boat): # current state

    side = "LEFT" if boat == 1 else "RIGHT"
    print(f"({lm},{lc},{boat}) | Boat on {side}")

# Start state space
start = (3, 3, 1)  # left_M, left_C, boat=1(left)
goal = (0, 0, 0)

# State space using SET (visited states)
visited = set()
queue = deque()

# Add start to queue and visited set
queue.append((start, [start]))
visited.add(start)

# Possible boat moves
moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

while queue:
    state, path = queue.popleft()  # BFS
    lm, lc, boat = state

    if state == goal:
        print(" GOAL REACHED")
        for i, s in enumerate(path):
            show_state(*s)
        break

    # Generate next states from current state
    right_m = M - lm
    right_c = C - lc

    if boat == 1:  # LEFT -> RIGHT
        for m, c in moves:
            if lm >= m and lc >= c and 1 <= m+c <= boat_max:
                new_lm = lm - m
                new_lc = lc - c
                new_boat = 0
                new_state = (new_lm, new_lc, new_boat)

                if safe_state(new_lm, new_lc) and new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))

    else:  # RIGHT -> LEFT
        for m, c in moves:
            if right_m >= m and right_c >= c and 1 <= m+c <= boat_max:
                new_lm = lm + m
                new_lc = lc + c
                new_boat = 1
                new_state = (new_lm, new_lc, new_boat)

                if safe_state(new_lm, new_lc) and new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))

