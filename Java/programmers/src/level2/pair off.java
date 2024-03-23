import java.util.Stack;

class Solution
{
    public int solution(String s)
    {
        Stack<Character> stack = new Stack<>();

        for(char c : s.toCharArray()) {
            if(!stack.isEmpty() && stack.peek() == c) {
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        if(stack.isEmpty()){
            return 1;
        }else{
            return 0;
        }


    }
}

/*
*  Stack을 활용한 문제풀이
*
*  느낀점 : 스택을 활용한 문제풀이를 하면 간단하게 풀릴 문제지만 문제 풀이를 생각해내는 것이 어렵게 느껴짐. 또한 스택이 아닌 문제풀이일 경우 효율성 문제가 나타난다.
* */