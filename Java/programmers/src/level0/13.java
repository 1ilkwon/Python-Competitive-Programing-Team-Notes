#include <stdio.h>
        #include <stdbool.h>
        #include <stdlib.h>

// s1_len은 배열 s1의 길이입니다.
// s2_len은 배열 s2의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
        int solution(String[] s1, String[] s2) {
        int answer = 0;
        for(int i=0; i<s2.length; i ++){
        if(s1[i].equals(s2[i])) {
        answer += 1;
        }
        }

        return answer;
        }