// 내가 짠 코드
function solution(N, K) {
    let count = 0;

    while (N > 1) {
        if(N % K === 0) {
            N = parseInt(N / K)
            count += 1
        } else {
            N -= 1
            count += 1
        }
    }
    return count;
}

// 답안 예시
function solution2(N, K) {
    let count = 0;
    
    while(true) {
        let target = parseInt(N / K) * K
        count += (N - target)

        if(N < K) break
        count += 1
        N = parseInt(N / K)
    }

    count += (N - 1)
    return count;
}

console.log(solution2(25, 5))