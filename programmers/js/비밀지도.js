function solution(n, arr1, arr2) {
    let answer = [];
    for(let i=0; i<n; i++) {
        let first = '0'.repeat(n - arr1[i].toString(2).length) + arr1[i].toString(2);
        let second = '0'.repeat(n - arr2[i].toString(2).length) + arr2[i].toString(2);
        
        let temp = '';
        for(let j=0; j<n; j++) {
            if(first[j] === '1' || second[j] === '1') {
                temp += '#'
            } else if(first[j] === '0' || second[j] === '0') {
                temp += ' '
            }
        }
        answer.push(temp);
        
    }
    return answer;
}