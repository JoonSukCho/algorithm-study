function solution(s) {
  var answer = [];
  let zero = 0;
  let count = 0;

  while (s !== "1") {
    let one = "";
    for (let i = 0; i < s.length; i++) {
      if (s[i] === "1") {
        one += "1";
      } else {
        zero++;
      }
    }

    count++;
    one = one.length.toString(2);
    s = one;
  }

  return [count, zero];
}
