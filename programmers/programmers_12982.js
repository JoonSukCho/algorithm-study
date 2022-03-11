function solution(d, budget) {
  var answer = 0;
  let money = 0;
  const sorted = d.sort((a, b) => a - b);

  for (let i = 0; i < sorted.length; i++) {
    money += sorted[i];
    if (budget < money) {
      answer = i;
      break;
    }

    answer = i + 1;
  }

  return answer;
}
