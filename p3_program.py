################################################
#   Team: Team 1                               #
#   Members: Karan Patal / Oscar(Jiaye) Fang   #
#           / Keuntae Kim / Edward Yeboah      #
#   Course: CSCI 6212 - 12                     #
#   Professor: Amrinder Arora                  #
#                 < Project >                  #
################################################
"""
- Problem #0
  - Teleportation in Astro haunted galaxies
    - You have a teleporter that can take you from galaxy i to galaxy j.
    Cost to teleport is given by c(i,j), which can be arbitrary. Some galaxies
    are “astro-haunted” - this is specified by a(i) which can be 0 or 1 (1 means
    that that galaxy is “astro-haunted”). Give a polynomial time algorithm that
    minimizes the cost of going from galaxy 1 to galaxy n, such that you pass
    through no more than k astro-haunted galaxies. (You can assume that galaxies
    1 and n are not astro-haunted.)
"""

from time import perf_counter_ns
from random import choice

######################
### First Solution ###
######################
def teleportation(n, k, a, c):    # findMinimumCost
    """
    <Pseudocode>
    // Step 1: Base Case
    Calculate D[i][j][0] as All Pairs Shortest path by ignoring the astro haunted galaxies.

    // Step 2: Inductive Step
    for kk = 1 to k
        for i = 1 to n
            for j = 1 to n
                Calculate D[i][j][kk] = min{D([i][j][kk-1], D[i][z][kk-1] + D[z][j][0] for all z such that a[z] = 1}

    """
    # Initialize the dynamic programming table
    D = [[float('inf') for _ in range(k + 1)] for _ in range(n)]

    # Initialize the base cases
    for j in range(k + 1):
        D[0][j] = 0

    # Dynamic programming to compute the minimum cost
    for i in range(1, n):
        for j in range(1, k + 1):
            if a[i] == 1:
                for x in range(i):
                    if a[x] == 1:
                        # print("BEFORE:::", dp[i][j], dp[x][j - 1] + c(x, i))
                        D[i][j] = min(D[i][j], D[x][j - 1] + c(x, i))
                        # print("MINIMUM:", dp[i][j])

    # The minimum cost to reach galaxy n from galaxy 1 with at most k astro-haunted galaxies
    return D[n - 1][k]

#######################
### Second Solution ###
#######################
def teleportation_2(n, k, a, c):  # minimum cost
    """
    <Pseudocode>
    // Step 1: Base Case
    Calculate D[i][j][0] as All Pairs Shortest path by ignoring the astro haunted galaxies.

    // Step 2: Inductive Step
    for kk = 1 to k
        for i = 1 to n
            for j = 1 to n
                Calculate D[i][j][kk] = min{D([i][j][kk-1], D[i][z][kk-1] + D[z][j][0] for all z such that a[z] = 1}

    """
    # Step 1: Initialize D for k=0 (base case)
    D = [[[float('inf')] * (k+1) for _ in range(n)] for _ in range(n)]
    print(D)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                print(f"{i},{j},hiiii")
                D[i][j][0] = 0
            elif a[i] == 1:
                print(f"this is 1, hiiii")
                D[i][j][0] = c[i][j]
                
    print(D)
    
    # Step 2: Dynamic Programming (Inductive Step)
    for kk in range(1, k+1):
        for i in range(n):
            for j in range(n):
                for z in range(n):
                    if a[z] == 1:
                        D[i][j][kk] = min(D[i][j][kk], D[i][z][kk - 1] + D[z][j][0])
    # Time Complexity: O(kn^3)
    
    return D[0][n - 1][k]


if __name__ == "__main__":
    ### First Solution ###
    ################################################################################################
    # # Example input values
    # n = 100
    # k = int(n * 0.1)
    # zero_and_ones = list(range(2))  # 1 means "astro-haunted"
    # a = [choice(zero_and_ones) for _ in range(n-2)]
    # a = [0] + a + [0]
    # c = lambda i, j: i + j  # A simple cost function for illustration
    
    # start = perf_counter_ns()
    # min_cost = teleportation(n, k, a, c)
    # end = perf_counter_ns()
    # print(f"Running time: {end - start} nanoseconds") ### Experimental result ###
    
    # # print(f"Minimum cost to travel from galaxy 1 to galaxy {n} with at most {k}")
    # # print(f"Minimum cost is {min_cost}")
    ################################################################################################
    
    ### Second Solution ###
    ################################################################################################
    # Example usage
    # n = 4   # Number of galaxies
    # k = 1   # Maximum allowed astro-haunted galaxies
    # a = [0, 1, 0, 1]
    # c = [[0, 5, 3, 2], [5, 0, 1, 6], [3, 1, 0, 4], [2, 6, 4, 0]]  # Teleportation cost matrix
    
    n = 10                                          # Number of galaxies
    k = int(n * 0.1)                                # Maximum allowed astro-haunted galaxies
    zero_and_ones = list(range(2))                  # List of 0 and 1
    a = [choice(zero_and_ones) for _ in range(n-2)] # Astro-haunted galaxies, a's total list size is the number of galaxies.
    a = [0] + a + [0]                               # Galaxies 1 and n are not astro-haunted.
    c = lambda i, j: i + j  # A simple Teleportation cost function

    start = perf_counter_ns()                         # start time
    result = teleportation_2(n, k, a, c)
    end = perf_counter_ns()                           # end time
    print(f"Running time: {end - start} nanoseconds") ### Experimental result ###
    
    print("Minimum cost to teleport:", result)      # Minimum cost
    ################################################################################################
