function solution(s) {

    s = s.split('');
    let answer = Number(s[0]);
    
    for(let i=1; i<s.length; i++) {
        // 0과 1일 경우 -> +
        if(s[i] === '0' || s[i] === '1') {
            answer += Number(s[i])
        } else { // 2부터 9일 경우 -> x
            answer *= Number(s[i])
        }
    }
    return answer;
}
console.log(solution('567'))