function solution(a, b) {
    var days = ['SUN','MON','TUE','WED','THU','FRI','SAT'];
    
    if (a < 10) {
        a = '0' + String(a);
    }
    
    if (b < 10) {
        b = '0' + String(b);
    }
    
    var date = '2016' + '-' + String(a) + '-' + String(b);
    var day = new Date(date).getDay();
    
    return days[day];
}