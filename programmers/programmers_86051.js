function solution(numbers) {
  const a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  const newA = a.filter((v) => !numbers.includes(v));

  let answer = 0;
  newA.forEach((v) => (answer += v));

  return answer;
}
