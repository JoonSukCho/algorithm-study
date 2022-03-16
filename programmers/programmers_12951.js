function solution(s) {
  var answer = "";
  let sArr = s.split(" ");

  for (let i = 0; i < sArr.length; i++) {
    sArr[i] = sArr[i].toLowerCase().split("");

    for (let j = 0; j < sArr[i].length; j++) {
      if (j === 0 && isNaN(sArr[i][j])) {
        sArr[i][j] = sArr[i][j].toUpperCase();
      }
    }
    sArr[i] = sArr[i].join("");
  }

  return sArr.join(" ");
}
