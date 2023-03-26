import java.util.*;

class Solution {
    public long solution(long n) {
        String ans = "";
        String str = String.valueOf(n);
        String[] arr = str.split("");
        Arrays.sort(arr,Collections.reverseOrder());
        for(int i=0; i<arr.length; i++){
            ans += arr[i];
        }
        long answer = Long.parseLong(ans);
        return answer;
    }
}