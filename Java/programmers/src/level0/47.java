class Solution {
    public int solution(int[] numbers) {
        int answer = Integer.MAX_VALUE * -1;
        int num =Integer.MAX_VALUE * -1;
        for(int i = 0; i <numbers.length; i++){
            for(int j=0; j< numbers.length; j++){
                if( i != j){
                    num = numbers[i] * numbers[j];
                }
                if(num >answer){
                    answer = num;
                }
            }
        }
        return answer;
    }
}