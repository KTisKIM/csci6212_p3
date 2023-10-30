public class p3_program_second {
    public static int minimumCostTeleportation(int n, int m, int[][] c, int[] a, int k) {
        // Step 1: Initialize D for k=0 (base case)
        int[][][] D = new int[n][n][k + 1];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    D[i][j][0] = 0;
                } else if (a[i] == 1) {
                    D[i][j][0] = c[i][j];
                }
            }
        }
        
        // Step 2: Dynamic Programming (Inductive Step)
        for (int kk = 1; kk <= k; kk++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    for (int z = 0; z < n; z++) {
                        if (a[z] == 1) {
                            D[i][j][kk] = Math.min(D[i][j][kk], D[i][z][kk - 1] + D[z][j][0]);
                        }
                    }
                }
            }
        }
        
        return D[0][n - 1][k];
    }

    public static void main(String[] args) {
        // Example usage
        int n = 4;  // Number of galaxies
        int m = 2;  // Number of galaxy pairs with teleportation cost
        int[][] c = {{0, 5, 3, 2}, {5, 0, 1, 6}, {3, 1, 0, 4}, {2, 6, 4, 0}};  // Teleportation cost matrix
        int[] a = {0, 1, 0, 1};  // Astro-haunted galaxies
        int k = 1;  // Maximum allowed astro-haunted galaxies

        long startTime = System.nanoTime();
        int result = minimumCostTeleportation(n, m, c, a, k);
        long endTime = System.nanoTime();
        long elapsedTime = endTime - startTime;

        System.out.println("Execution time: " + elapsedTime + " milliseconds");

        System.out.println("Minimum cost to teleport: " + result);
    }
}
