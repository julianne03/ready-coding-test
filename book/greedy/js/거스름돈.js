function solution(N) {
    const coin_type = [500, 100, 50, 10]

    // 루프를 돌면서 최대한 동전의 개수를 빨리 세기
    let count = 0;
    
    coin_type.forEach((coin, i) => {
        count += parseInt(N / coin_type[i])
        N = N % coin_type[i]
    })
    return count
}

console.log(solution(1260))