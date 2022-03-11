function solution(left, right) {
  var answer = 0;

  for (let i = left; i <= right; i++) {
    const yCount = getYCount(i);
    if (yCount % 2 === 0) {
      answer += i;
    } else {
      answer -= i;
    }
  }

  return answer;
}

function getYCount(n) {
  let yCount = 0;
  let idx = 1;

  while (idx <= n) {
    if (n % idx === 0) {
      yCount++;
    }
    idx++;
  }

  return yCount;
}
