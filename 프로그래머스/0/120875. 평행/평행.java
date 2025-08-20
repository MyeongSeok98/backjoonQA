class Solution {
    public int solution(int[][] dots) {
        return (parallel(dots, 0, 1, 2, 3) ||
                parallel(dots, 0, 2, 1, 3) ||
                parallel(dots, 0, 3, 1, 2)) ? 1 : 0;
    }

    private boolean parallel(int[][] d, int a, int b, int c, int e) {
        long x1 = (long)d[b][0] - d[a][0];
        long y1 = (long)d[b][1] - d[a][1];
        long x2 = (long)d[e][0] - d[c][0];
        long y2 = (long)d[e][1] - d[c][1];
        return y1 * x2 == y2 * x1;
    }
}