function solution(lottos, win_nums) {
    
    const rank = [6, 6, 5, 4, 3, 2, 1]
    
    const same_nums = lottos.filter((lotto) => win_nums.includes(lotto))
    let count_zero = lottos.filter((d) => d === 0).length;
    
    const max_rank = rank[same_nums.length + count_zero]
    const min_rank = rank[same_nums.length]
    
    return [max_rank, min_rank];
}