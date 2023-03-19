class Solution {
    public int solution(int n) {
        int answer = 100;
        for(int i=1; i <=100; i++){
            if((i*6)%n ==0 && i <= answer){
                answer = i;
            }
        }
        return answer;
    }
}ㄴSt