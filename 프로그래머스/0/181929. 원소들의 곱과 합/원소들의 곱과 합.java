class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int a1 = 0;
        int a2 = 1;
        
        for(int i : num_list){
            a1 += i;
        }
        for(int i : num_list){
            a2 *= i;
        }
        
        a1 *= a1;
        if(a1 > a2)
            answer = 1;
        return answer;
    }
}