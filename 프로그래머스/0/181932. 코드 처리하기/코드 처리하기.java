class Solution {
    public String solution(String code) {
        StringBuilder sb = new StringBuilder();
        boolean mode = false;
        char[] ca = code.toCharArray();
        for(int i = 0; i < code.length(); i++){
            if(ca[i] == '1'){
                mode = !mode;
            }
            else{
                if(!mode && i % 2 == 0){
                    sb.append(ca[i]);
                }
                else if(mode && i % 2 == 1){
                    sb.append(ca[i]);
                }
            }
        }
        
        String answer = sb.toString();
        if(answer.equals(""))
            return "EMPTY";
        return answer;
    }
}