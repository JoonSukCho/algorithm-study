function solution(answers) {
    var supo_1 = [1, 2, 3, 4, 5];    
    var supo_2 = [2, 1, 2, 3, 2, 4, 2, 5];
    var supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    var count = [0, 0, 0];
    
    for (var i = 0; i < answers.length; i++) {
        if(supo_1[i % supo_1.length] === answers[i]) {
            count[0]++;
        }
        
        if(supo_2[i % supo_2.length] === answers[i]) {
            count[1]++;
        }
        
        if(supo_3[i % supo_3.length] === answers[i]) {
            count[2]++;
        }
    }
    
    var max_count = Math.max(count[0], count[1], count[2]);
    var result = [];
    for(var i = 0; i < 3; i++) {
        if(max_count === count[i]) {
            result.push(i + 1);
        }
    }

    return result;
}
