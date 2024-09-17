class Solution {
    public int solution(int order) {
        int answer = 0;
        String strorder = "" + order;

        for(int i=0; i<strorder.length(); i++){
            if( strorder.charAt(i) == '3' || strorder.charAt(i) == '6'
                    || strorder.charAt(i) == '9' ){
                answer ++;
            }
        }
        return answer;
    }
}