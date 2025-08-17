class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        for(int i = 0; i < queries.length; i++){
            int minN = 10000001;
            for(int j = queries[i][0]; j <= queries[i][1]; j++){
                if(arr[j] > queries[i][2] ){
                    minN = Math.min(minN, arr[j]);
                }
            }
            if(minN == 10000001)
                minN = -1;
            answer[i] = minN;
        }
        return answer;
    }
}