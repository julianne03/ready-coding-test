function solution(answers) {
    const first = [1, 2, 3, 4, 5];
    const second = [2, 1, 2, 3, 2, 4, 2, 5]
    const third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    let result = [];
    
    const first_count = answers.filter((a, index) => a === first[index%first.length]).length
    const second_count = answers.filter((a, index) => a === second[index%second.length]).length
    const third_count = answers.filter((a, index) => a === third[index%third.length]).length
    
    const max_count = Math.max(first_count, second_count, third_count);
    
    if (first_count === max_count) result.push(1);
    if (second_count === max_count) result.push(2);
    if (third_count === max_count) result.push(3);
    
    return result;
}