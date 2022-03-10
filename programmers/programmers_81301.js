function solution(s) {
  const num = {
    zero: 0,
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9,
  };

  const strArr = s.split("");
  let str = "";
  let numStr = "";
  for (let i = 0; i < strArr.length; i++) {
    if (!Number.isNaN(parseInt(strArr[i], 10))) {
      numStr += strArr[i];
    } else {
      str += strArr[i];

      for (const key in num) {
        if (str === key) {
          numStr += num[str];
          str = "";
        }
      }
    }
  }

  return parseInt(numStr, 10);
}
