class Solution {
    public int[] solution(int[] emergency) {
        int seq = 1;
        int[] answer = new int[emergency.length];
        for(int i=0; i<emergency.length; i++){
            for(int j=0; j<emergency.length; j++){
                if(emergency[i] < emergency[j]){
                    seq++;
                }
            }
            answer[i]=seq;
            seq = 1;
        }
        return answer;
    }
}