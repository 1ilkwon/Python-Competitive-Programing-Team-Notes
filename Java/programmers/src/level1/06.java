import java.lang.Math;

class Solution {
    public long solution(long n) {
        long answer = 0;
        long m = (long)Math.sqrt(n);
        if(m*m == n){
            answer = (m+1)*(m+1);
        }else{
            answer = -1;
        }
        return answer;
    }
}