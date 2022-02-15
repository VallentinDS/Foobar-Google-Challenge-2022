# As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. 
# It's not easy building a doomsday device and ordering the bunnies around at the same time, after all! 
# In order to make sure that everyone is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. 
# It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. 
# That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. 
# Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

# To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters: 
# the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  
# The function should return an integer representing the smallest number of moves it will take for you to travel from the source 
# square to the destination square using a chess knight's moves (that is, two squares in any direction 
# immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  
# Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------

# Languages
# =========

# To provide a Python solution, edit solution.py
# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution(0, 1)
# Output:
#     3

# Input:
# solution.solution(19, 36)
# Output:
#     1


def solution(s, d):
    # getting the coordinates of the source and destination
    s_coord = divmod(s, 8)
    d_coord = divmod(d, 8)

    def l_moves(x, y):
        possible_paths = [
            (x+2, y+1), (x+2, y-1),
            (x-2, y+1), (x-2, y-1),
            (x+1, y+2), (x+1, y-2),
            (x-1, y+2), (x-1, y-2)
            ]

        paths = []
        for a, b in possible_paths:
            # check if the coordinates are on the board and not outsiode it
            if 0 <= a < 8 and 0 <= b < 8:
                paths.append((a, b))
        
        return paths

    def count_moves(s_coord, d_coord):
        if s_coord == d_coord:
        # base case
            return 0
        
        from collections import deque
        x = s_coord[0]
        y = s_coord[1]
        q = deque([(x, y, 0)])
        visited = {(x, y):1}

        while q:
            u, v , count = q.popleft()
            paths = l_moves(u, v)
            for p in paths:
                if p == d_coord:
                    return count+1
                if p not in visited:
                    visited[p] = 1
                    q.append((p[0], p[1], count+1))
        return -1
    
    return count_moves(s_coord, d_coord)

solution(3, 6)