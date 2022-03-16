function solution(s) {
  var answer = 0;

  const sArr = s.split("");

  let i = 0;
  while (i < sArr.length) {
    if (check(sArr)) {
      answer++;
    }

    i++;
    sArr.push(sArr.shift());
  }

  return answer;
}

function check(sArr) {
  if ([")", "}", "]"].includes(sArr[0])) return false;
  if (["(", "{", "["].includes(sArr[sArr.length - 1])) return false;

  let big = 0;
  let medium = 0;
  let small = 0;
  for (let i = 0; i < sArr.length; i++) {
    if (sArr[i] === "[") {
      if ([")", "}"].includes(sArr[i + 1])) {
        big = 1;
        break;
      }
      big++;
    }
    if (sArr[i] === "]" && big > 0) {
      big--;
    }
    if (sArr[i] === "{") {
      if ([")", "]"].includes(sArr[i + 1])) {
        medium = 1;
        break;
      }

      medium++;
    }
    if (sArr[i] === "}" && medium > 0) {
      medium--;
    }
    if (sArr[i] === "(") {
      if (["}", "]"].includes(sArr[i + 1])) {
        small = 1;
        break;
      }

      small++;
    }
    if (sArr[i] === ")" && small > 0) {
      small--;
    }
  }

  return big === 0 && medium === 0 && small === 0;
}
