class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        int dice[] = new int[7];
        boolean count[] = new boolean[7];
        dice[a]++;
        dice[b]++;
        dice[c]++;
        dice[d]++;
        
        int p;
        int q;
        for(int i = 1; i <= 6; i++){
            if(dice[i] == 4){
                answer = i * 1111;
                return answer;
            }
            if(dice[i] == 1){
                count[i] = true;
            }
            else if(dice[i] == 2){
                p = i;
                int sub = 1;
                for(int j = 1; j <= 6; j++){
                    if(dice[j] == 1){
                        sub *= j;
                    }
                    else if(dice[j] == 2 && i != j){
                        q = j;
                        answer = (p + q) * Math.abs(p - q);
                        return answer;
                    }
                }
                answer = sub;
                return answer;
            }
            else if(dice[i] == 3){
                p = i;
                for(int j = 1; j <= 6; j++){
                    if(dice[j] == 1){
                        q = j;
                        answer = (10 * p) + q;
                        answer *= answer;
                    }
                }
                return answer;
            }
        }
        for(int j = 1; j <= 6; j++){
            if(count[j]){
                return j;
            }
        }
        return answer;
    }
}