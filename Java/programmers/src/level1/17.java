import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int p_num = 0;
        int y_num = 0;
        char ch = ' ';
        for (int i = 0; i < s.length(); i++) {
            ch = s.charAt(i);
            if(ch == 'p'|| ch == 'P'){
                p_num++;
            }else if(ch == 'y'|| ch=='Y'){
                y_num++;
            }
        }
        if(p_num != y_num){
            answer = false;
        }
        return answer;
    }
}