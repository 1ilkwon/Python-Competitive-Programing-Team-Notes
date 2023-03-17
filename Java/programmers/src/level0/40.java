class Solution {
    public int solution(int hp) {
        int answer = 0;
        int cap = hp / 5;
        hp = hp % 5;
        int sol = hp / 3;
        hp = hp % 3;
        answer = hp + sol + cap;
        return answer;
    }
}