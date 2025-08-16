class Solution {
    public int solution(int a, int b) {
        StringBuilder sb = new StringBuilder();
        
        sb.append(a);
        sb.append(b);
        int num1 = Integer.parseInt(sb.toString());
        int num2 = 2 * a * b;
        
        if(num1 > num2)
            return num1;
        else
            return num2;
    }
}