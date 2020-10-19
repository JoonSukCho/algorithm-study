function solution(s) {
    var arr = s.split(' ');
    var a = [];
    var text = '';
    for(var i = 0; i < arr.length; i++) {
        var k = '';
        text = arr[i];
        for(var j = 0; j < text.length; j++) {
            if(j % 2 === 0) {
                k += text[j].toUpperCase();
            }
            else {
                k += text[j].toLowerCase();
            }
        }
        a.push(k);
    }
    
    return a.join(' ');
}