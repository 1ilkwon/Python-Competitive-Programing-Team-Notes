public int solution(int n) {
        int answer = 0;
        // 소수 판별을 위한 boolean타입 배열 선언
        boolean[] prime = new boolean [n+1];
        for(int i=2; i<=n ; i++)
        prime[i]=true;

        // n의 제곱근 root
        int root=(int)Math.sqrt(n);


        //범위를 제곱근으로 설정
        for(int i=2; i<=root; i++){
        //i가 소수일 경우 그 배수를 false로 전환
        if(prime[i]==true){
        for(int j=i; i*j<=n; j++) {
        prime[i*j]=false;
        }
        }

        // prime배열의 인덱스값이 false일 경우 counting
        for(int i =2; i<=n; i++) {
        if(prime[i]==true)
        answer++;
        }
        return answer;
        }