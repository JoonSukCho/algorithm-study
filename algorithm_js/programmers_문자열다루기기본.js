function solution(s) {
    if(s.length === 4 || s.length === 6) {
        var a = true;
        
        for (var i = 0; i < s.length; i++) {
            if(isNaN(s[i])) {
                a = false;
            }
        }
        
        return a;
    }
    
    else return false;
}