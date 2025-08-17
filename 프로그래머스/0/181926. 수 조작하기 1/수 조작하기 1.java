class Solution {
    public int solution(int n, String control) {
        char[] ca = control.toCharArray();
        
        for(char c : ca){
            if(c == 'w'){
                n += 1;
            }
            else if(c == 's'){
                n += -1;
            }
            else if(c == 'd'){
                n += 10;
            }
            else if(c == 'a'){
                n += -10;
            }
        }
        int answer = n;
        return answer;
    }
}