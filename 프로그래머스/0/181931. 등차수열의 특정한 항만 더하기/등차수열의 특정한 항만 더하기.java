class Solution {
    public int solution(int a, int d, boolean[] included) {
        int sum = 0;
        int n = a;
        for(int i = 0; i < included.length; i++){
            if(included[i]){
                sum+= n;
            }
            n += d;
        }
        int answer = sum;
        return answer;
    }
}