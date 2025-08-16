class Solution {
    public int solution(int a, int b) {
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        sb1.append(a);
        sb1.append(b);
        sb2.append(b);
        sb2.append(a);
        
        int answer1 = Integer.parseInt(sb1.toString());
        int answer2 = Integer.parseInt(sb2.toString());
        
        if(answer1 > answer2)
            return answer1;
        else
            return answer2;
    }
}