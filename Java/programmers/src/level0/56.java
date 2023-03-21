class Solution {
    public int solution(int num, int k) {
        int answer = -1;
        String str = "" + num;

        answer = str.indexOf(String.valueOf(k));
        if(answer != -1){
            answer++;
        }

        return answer;
    }
}