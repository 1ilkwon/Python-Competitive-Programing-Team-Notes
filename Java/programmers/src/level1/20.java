class Solution {
    public String solution(int n) {
        String answer = "";
        for(int j=0; j<(n/2); j++){
            answer += "수박";
        }
        if(n%2 != 0){
            answer += "수";
        }
        return answer;
    }
}