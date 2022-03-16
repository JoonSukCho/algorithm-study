function solution(n, a, b) {
  let answer = 0;
  const users = [];

  for (let i = 1; i <= n; i++) {
    users.push(i);
  }

  let flag = true;
  while (flag) {
    answer++;
    for (let i = 0; i < users.length; i += Math.pow(2, answer)) {
      const match = users.slice(i, i + Math.pow(2, answer));
      if (match.includes(a) && match.includes(b)) {
        flag = false;
        break;
      }
    }
  }

  return answer;
}
