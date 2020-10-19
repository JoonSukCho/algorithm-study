function solution(phone_number) {
    var arr = [];

    for(var i = 0; i < phone_number.length; i++) {
        if(i < phone_number.length - 4) {
            arr.push('*');
        }

        else {
            arr.push(phone_number[i])
        }
    }

    console.log(arr.join(''));
    
    return arr.join('');
}

solution('01033334444');