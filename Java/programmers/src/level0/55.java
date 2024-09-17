import java.lang.Math;
import java.util.*;
class Solution {laq(
        public int[] solution(int n) {
    int[] answer = {};
    int index = 0;
    ArrayList<Integer> ar = new ArrayList<>();

    for(int i=1; i <= Math.sqrt(n); i++){
        if(n % i == 0){
            ar.add(i);
            if(i * i !=n){
                ar.add(n/i);
            }
        }
    }

    answer = new int[ar.size()];
    for(int i = 0; i<ar.size(); i++){
        answer[i] = ar.get(i);
    }
    Arrays.sort(answer);
    return answer;
}
}