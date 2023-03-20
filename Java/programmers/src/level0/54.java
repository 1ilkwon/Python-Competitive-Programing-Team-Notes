import java.util.*;

class Solution {
    public String solution(String my_string) {
        String answer = "";
        String an = "";
        an = my_string.toLowerCase();
        //System.out.println(answer);
        String [] str = an.split("");
        Arrays.sort(str);
        for(String a : str){
            answer = answer.concat(a);
        }
        return answer;
    }
}