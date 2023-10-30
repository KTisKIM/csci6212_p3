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
### first solution ###
######################
def findMinimumCost(n, k, a, c):
    # Initialize the dynamic programming table
    # dp = [[float('inf') for _ in range(k + 1)] for _ in range(n)]
    dp = [[0 for _ in range(k + 1)] for _ in range(n)]

    # Initialize the base cases
    for j in range(k + 1):
        dp[0][j] = 0

    # Dynamic programming to compute the minimum cost
    for i in range(1, n):
        for j in range(1, k + 1):
            if a[i] == 1:
                for x in range(i):
                    if a[x] == 1:
                        # print("BEFORE:::", dp[i][j], dp[x][j - 1] + c(x, i))
                        dp[i][j] = min(dp[i][j], dp[x][j - 1] + c(x, i))
                        # print("MINIMUM:", dp[i][j])

    # The minimum cost to reach galaxy n from galaxy 1 with at most k astro-haunted galaxies
    return dp[n - 1][k]

#######################
### Second Solution ###
#######################
def teleportation(n, m, c, a, k):  # minimum cost
	"""
  	<Pseudocode>
	// Step 1: Base Case
	Calculate D[i][j][0] as All Pairs Shortest path by ignoring the astro haunted galaxies.

	// Step 2: Inductive Step
	for k = 1 to m
		for i = 1 to n
			for j = 1 to n
				Calculate D[i][j][k] = min {D([i][j][k-1], D[i][z][k-1] + D[z][j][0] for all z such that A[z] = 1}
    
	"""

if __name__ == "__main__":
    ### First Solution ###
    ################################################################################################
    # Example input values
    n = 100
    k = int(n * 0.1)
    # a = [0, 1, 1, 0, 1]  # 1 means "astro-haunted"
    zero_and_ones = list(range(2))  # 1 means "astro-haunted"
	# zero_to_nine = list(range(10))                  # numbers between 0-9 for the input array.
    # a = [choice(zero_and_ones) for i in range(n)]    # array of numbers based on the size of 'n'
    a = [choice(zero_and_ones) for _ in range(n-2)]
    a = [0] + a + [0]
    c = lambda i, j: i + j  # A simple cost function for illustration

    
    # print("what are you:", a)
    
    start = perf_counter_ns()
    min_cost = findMinimumCost(n, k, a, c)
    end = perf_counter_ns()
    print(f"Running time: {end - start} nanoseconds") ### Experimental result ###
    
    # print(f"Minimum cost to travel from galaxy 1 to galaxy {n} with at most {k}")
    # print(f"Minimum cost is {min_cost}")
    ################################################################################################
    
    ### Second Solution
    ################################################################################################
    
    ################################################################################################
