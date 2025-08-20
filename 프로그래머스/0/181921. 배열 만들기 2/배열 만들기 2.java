class Solution {
    public int[] solution(int l, int r) {
        int count = 0;
        for(int i = l; i <= r; i++){
            boolean b = false;
            String str = String.valueOf(i);
            for(int j = 0; j < str.length(); j++){
                if(str.charAt(j) != '5' && str.charAt(j) != '0'){
                    b = true;
                }
            }
            if(b) continue;
            count++;
        }
        if(count == 0) {
            int[] answer = new int[]{-1};
            return answer;
        }
        int[] answer = new int[count];
        int n = 0;
        for(int i = l; i <= r; i++){
            boolean b = false;
            String str = String.valueOf(i);
            for(int j = 0; j < str.length(); j++){
                if(str.charAt(j) != '5' && str.charAt(j) != '0'){
                    b = true;
                }
            }
            if(b) continue;
            answer[n] = i;
            n++;
        }
        return answer;
    }
}