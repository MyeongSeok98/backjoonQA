class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        
        int top = 0;
        int bottom = n-1;
        int left = 0;
        int right = n-1;
        int v = 1;
        while(top <= bottom && left <= right){
            for(int i = left; i <= right; i++ ){
                answer[top][i] = v++;
            }
            top++;
            
            for(int i = top; i <= bottom; i++){
                answer[i][right] = v++;
            }
            right--;
            
            if (top <= bottom) {
                for (int j = right; j >= left; j--) answer[bottom][j] = v++;
                bottom--;
            }
            if (left <= right) {
                for (int i = bottom; i >= top; i--) answer[i][left] = v++;
                left++;
            }
        }
        return answer;
    }
}