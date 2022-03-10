function solution(N, stages) {
  const answer = [];

  for (let i = 1; i <= N; i++) {
    answer.push(i);
  }

  let failPercent = answer.map((v) => {
    let totalCount = 0;
    let failCount = 0;

    stages.forEach((stage) => {
      if (stage >= v) {
        totalCount++;
      }

      if (stage === v) {
        failCount++;
      }
    });

    return { stage: v, fail: failCount / totalCount };
  });

  const sorted = failPercent.sort((a, b) => b.fail - a.fail);

  return sorted.map((v) => v.stage);
}
