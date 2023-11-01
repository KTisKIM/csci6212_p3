import random
import time
import sys


def pairs_shortest_path(D, A, n):
    """
    Pairs Shortest Path by eliminating all astro-haunted galaxies

    Parameters
    ----------
    D : 3D array
        D[i][j][k] is the shortest path from i to j with k astro-haunted galaxies
    A : 1D array
        A[i] is the astro-haunted galaxy, 1 is astro-haunted, 0 is not
    n : int
        number of galaxies
    """
    for k in range(n):
        if A[k] == 1:  # skip astro-haunted galaxies
            continue
        for i in range(n):
            for j in range(n):
                D[i][j][0] = min(D[i][j][0], D[i][k][0] + D[k][j][0])
    return D


def shortest_path_astro_haunted(D, A, n, m):
    """
    Shortest Path with astro-haunted galaxies

    Parameters
    ----------
    D : 3D array
        D[i][j][k] is the shortest path from i to j with k astro-haunted galaxies
    A : 1D array
        A[i] is the astro-haunted galaxy, 1 is astro-haunted, 0 is not
    n : int
        number of galaxies
    """
    for k in range(1, m + 1):  # k is the number of astro-haunted galaxies, from 1 to m
        for i in range(n):
            for j in range(n):
                D[i][j][k] = D[i][j][k - 1]
                for z in range(n):
                    if A[z] == 0:  # skip non-astro-haunted galaxies
                        continue
                    D[i][j][k] = min(D[i][j][k], D[i][z][k - 1] + D[z][j][0])
    return D


def run(n, m, A, cost):
    """
    Run the algorithm
    """
    D = [[[float("inf") for _ in range(m + 1)] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                D[i][j][0] = 0
            else:
                D[i][j][0] = cost[i][j]
    D = pairs_shortest_path(D, A, n)
    print("After eliminating astro-haunted galaxies: " + str(D[0][n - 1][0]))
    D = shortest_path_astro_haunted(D, A, n, m)
    print("After adding astro-haunted galaxies: " + str(D[0][n - 1][m]))
    return D[0][n - 1][m]


def test_run_time(n, m, prob):
    """
    Test the run time of the algorithm
    """
    cost = [[float("inf") for _ in range(n)] for _ in range(n)]
    A = [1 if random.random() < prob else 0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cost[i][j] = random.randint(10, 1000)
    start = time.time()
    run(n, m, A, cost)
    end = time.time()
    print("n = {}, m = {}, prob = {}, run time = {}".format(n, m, prob, end - start))


# python3 teleportation.py n m prob
# python3 teleportation.py 10 3 0.3
if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    prob = float(sys.argv[3])
    if (prob < 0) or (prob > 1):
        print("Probability must be between 0 and 1")
        sys.exit(1)
    test_run_time(int(sys.argv[1]), m, prob)
