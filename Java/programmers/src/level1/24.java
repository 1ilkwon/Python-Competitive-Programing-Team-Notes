class Solution {
    public boolean solution(String s) {
        boolean answer = true;
        if(s.length()==4 || s.length()==6){
            try{
                Integer.parseInt(s);
                return answer;
            }catch(NumberFormatException ex){
                return answer = false;
            }
        }else{
            return answer = false;
        }
    }
}