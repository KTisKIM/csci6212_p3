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
    are “astro-haunted” – this is specified by a(i) which can be 0 or 1 (1 means
    that that galaxy is “astro-haunted”). Give a polynomial time algorithm that
    minimizes the cost of going from galaxy 1 to galaxy n, such that you pass
    through no more than k astro-haunted galaxies. (You can assume that galaxies
    1 and n are not astro-haunted.)
"""

def teleportation():
	"""
  	Pseudocode:
	// Step 1: Base Case
	Calculate D[i][j][0] as All Pairs Shortest path by ignoring the astro haunted galaxies.

	// Step 2: Inductive Step
	for k = 1 to m
		for i = 1 to n
			for j = 1 to n
				Calculate D[i][j][k] = min {D([i][j][k-1], D[i][z][k-1] + D[z][j][0] for all z such that A[z] = 1}
	"""
	# Step 1: Base Case
	# Calculate D[i][j][0] as All Pairs Shortest path by ignoring the astro haunted galaxies.

	# Step 2: Inductive Step
	# for k = 1 to m
	# 	for i = 1 to n
	# 		for j = 1 to n
	# 			Calculate D[i][j][k] = min {D([i][j][k-1], D[i][z][k-1] + D[z][j][0] for all z such that A[z] = 1}
	None

if __name__ == "__main__":
    None
