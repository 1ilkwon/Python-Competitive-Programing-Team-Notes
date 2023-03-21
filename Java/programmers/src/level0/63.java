class Solution {
    public int solution(int n) {
        int answer = 0;
        for(int i=1; i<=10; i++){
            if(fact(i)<=n){
                answer = i;
                continue;
            }else{
                break;
            }
        }
        return answer;
    }

    private static int fact(int m){
        if(m > 1){
            return m * fact(m-1);
        }
        return m;
    }
}