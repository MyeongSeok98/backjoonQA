import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        StringBuilder result = new StringBuilder();
        
        for(char c : a.toCharArray()){
            if(Character.isUpperCase(c))
                result.append(Character.toLowerCase(c));
            else
                result.append(Character.toUpperCase(c));
        }
        
        System.out.println(result.toString());
    }
}