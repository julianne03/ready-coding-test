function solution(n, m) {
    if(n > m) {
        let temp = n;
        n = m;
        m = temp;
    }
    const max = getMax(n, m);
    const min = getMin(n, m);
    
    return [max, min];
}

function getMax(n, m) {
    for(let i=m; i>=1; i--) {
        if(m % i === 0 && n % i === 0) return i;
    }
}

function getMin(n, m) {
    for(let i=n; i<=n*m; i++) {
        if(i % n === 0 && i % m === 0) return i;
    }
}