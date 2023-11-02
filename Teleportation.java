/***********************************************/
/*   Team: Team 1                              */
/*   Members: Karan Patal / Oscar(Jiaye) Fang  */
/*           / Keuntae Kim / Edward Yeboah     */
/*   Course: CSCI 6212 - 12                    */
/*   Professor: Amrinder Arora                 */
/*                < Project 3 >                */
/***********************************************/

// - Problem #0
//   - Teleportation in Astro haunted galaxies
//     - You have a teleporter that can take you from galaxy i to galaxy j.
//     Cost to teleport is given by c(i,j), which can be arbitrary. Some galaxies
//     are “astro-haunted” - this is specified by a(i) which can be 0 or 1 (1 means
//     that that galaxy is “astro-haunted”). Give a polynomial time algorithm that
//     minimizes the cost of going from galaxy 1 to galaxy n, such that you pass
//     through no more than k astro-haunted galaxies. (You can assume that galaxies
//     1 and n are not astro-haunted.)

// <Pseudocode>
// // Step 1: Base Case
// Calculate D[i][j][0] as All Pairs Shortest path by ignoring the astro haunted galaxies.
//
// // Step 2: Inductive Step
// for kk = 1 to k
//     for i = 1 to n
//         for j = 1 to n
//             Calculate D[i][j][kk] = min{D([i][j][kk-1], D[i][z][kk-1] + D[z][j][0] for all z such that a[z] = 1}


import java.util.Arrays;
import java.util.Random;

public class Teleportation {
    public static int[][][] pairsShortestPath(int[][][] D, int[] A, int n) {
        for (int k = 0; k < n; k++) {
            if (A[k] == 1) {
                continue;  // skip astro-haunted galaxies
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    D[i][j][0] = Math.min(D[i][j][0], D[i][k][0] + D[k][j][0]);
                }
            }
        }
        return D;
    }

    public static int[][][] shortestPathAstroHaunted(int[][][] D, int[] A, int n, int m) {
        for (int k = 1; k <= m; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    D[i][j][k] = D[i][j][k - 1];
                    for (int z = 0; z < n; z++) {
                        if (A[z] == 0) {
                            continue;  // skip non-astro-haunted galaxies
                        }
                        D[i][j][k] = Math.min(D[i][j][k], D[i][z][k - 1] + D[z][j][0]);
                    }
                }
            }
        }
        return D;
    }

    public static int run(int n, int m, int[] A, int[][] cost) {
        int[][][] D = new int[n][n][m + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    D[i][j][0] = 0;
                } else {
                    D[i][j][0] = cost[i][j];
                }
            }
        }
        D = pairsShortestPath(D, A, n);
        System.out.println("After eliminating astro-haunted galaxies: " + D[0][n - 1][0]);
        D = shortestPathAstroHaunted(D, A, n, m);
        System.out.println("After adding astro-haunted galaxies: " + D[0][n - 1][m]);
        return D[0][n - 1][m];
    }

    public static void testRunTime(int n, int m, double prob) {
        int[][] cost = new int[n][n];
        int[] A = new int[n];
        Random random = new Random();
        for (int i = 0; i < n; i++) {
            A[i] = random.nextDouble() < prob ? 1 : 0;
            for (int j = 0; j < n; j++) {
                cost[i][j] = random.nextInt(991) + 10; // Generates a random number between 10 and 1000
            }
        }
        long startTime = System.nanoTime();
        run(n, m, A, cost);
        long endTime = System.nanoTime();
        System.out.println("n = " + n + ", m = " + m + ", prob = " + prob + ", run time = " + 
(endTime - startTime));
    }

    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int m = (int) (n * 0.1);
        double prob = 0.3;
        testRunTime(n, m, prob);
    }
}
