#include <stdio.h>
        #include <stdbool.h>
        #include <stdlib.h>

        double solution(int[] numbers) {
        double answer = 0;
        //배열의 모든 정수 더하기
        for (int i=0;i<numbers.length;i++)
        answer += numbers[i];
        return answer/numbers.length;
        }