function solution(s) {
    var leng = s.length;
    var answer = '';
    
    if(leng % 2 === 0) {
        answer = s[(leng / 2) - 1] + s[leng / 2];
    }
    
    else {
        answer = s[Math.floor(leng / 2)];
    }
    
    return answer;
}