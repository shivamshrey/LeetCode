// 1686. Stone Game VI

class Solution {
    public int stoneGameVI(int[] aliceValues, int[] bobValues) {
        int n = aliceValues.length;
        int[][] sums = new int[n][];
        for (int i = 0; i < n; i++) {
            sums[i] = new int[] {aliceValues[i] + bobValues[i], aliceValues[i], bobValues[i]};
        }
        Arrays.sort(sums, (a, b) -> Integer.compare(b[0], a[0]));
        int alice = 0;
        int bob = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                alice += sums[i][1];
            } else {
                bob += sums[i][2];
            }
        }
        return Integer.compare(alice, bob);
    }
}
