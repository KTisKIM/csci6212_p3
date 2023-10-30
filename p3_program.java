import java.util.Random;

public class p3_program {

    public static int findMinimumCost(int n, int k, int[] a, CostFunction c) {
        int[][] dp = new int[n][k + 1];

        // Initialize the base cases
        for (int j = 0; j <= k; j++) {
            dp[0][j] = 0;
        }

        // Dynamic programming to compute the minimum cost
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                if (a[i] == 1) {
                    for (int x = 0; x < i; x++) {
                        if (a[x] == 1) {
                            dp[i][j] = Math.min(dp[i][j], dp[x][j - 1] + c.cost(x, i));
                        }
                    }
                }
            }
        }

        // The minimum cost to reach galaxy n from galaxy 1 with at most k astro-haunted galaxies
        return dp[n - 1][k];
    }

    public static void main(String[] args) {
        int n = 100;
        int k = (int) (n * 0.1);
        int[] a = new int[n];
        Random random = new Random();
        for (int i = 0; i < n - 2; i++) {
            a[i + 1] = random.nextInt(2); // 0 or 1
        }

        int[][] dp = new int[n][k + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= k; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }

        long startTime = System.nanoTime();
        int minCost = findMinimumCost(n, k, a, (i, j) -> i + j);
        long endTime = System.nanoTime();
        long elapsedTime = endTime - startTime;

        System.out.println("Execution time: " + elapsedTime + " milliseconds");

        System.out.println("Minimum cost is " + minCost);
    }

    @FunctionalInterface
    interface CostFunction {
        int cost(int i, int j);
    }
}
