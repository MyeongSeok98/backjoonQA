class Solution {
    public int[][] solution(int[][] arr) {
        int row = arr.length;
        int column = arr[0].length;
        int [][] answer = {};
        if(row > column){
            answer = new int[row][row];
            for(int i = 0; i < row; i++){
                   for(int j = 0; j < row; j++){
                       if(j < column)
                           answer[i][j] = arr[i][j];
                       else
                           answer[i][j] = 0;
                   }
            }
        }
        else{
            answer = new int[column][column];
            for(int i = 0; i < column; i++){
                for(int j = 0; j < column; j++){
                       if(i < row)
                           answer[i][j] = arr[i][j];
                       else
                           answer[i][j] = 0;
                   }
            }
        }
        return answer;
    }
}