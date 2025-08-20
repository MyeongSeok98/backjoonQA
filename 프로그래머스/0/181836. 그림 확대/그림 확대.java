class Solution {
    public String[] solution(String[] picture, int k) {
        int xL = picture[0].length();
        int yL = picture.length;
        char[][] canvas = new char[yL * k][xL * k];
        for(int i = 0; i < yL; i++){
            for(int j = 0; j < xL; j++){
                int startY = i * k;
                int endY = ((i+1) * k);
                int startX = j * k;
                int endX = ((j+1) * k); 
                char c = picture[i].charAt(j);
                for(int y = startY; y < endY; y++){
                    for(int x = startX; x < endX; x++){
                        canvas[y][x] = c;
                    }
                }
            }
        }
        
        String[] answer = new String[yL * k];
        for (int y = 0; y < answer.length; y++) {
            answer[y] = new String(canvas[y]);
        }
        return answer;
    }
}