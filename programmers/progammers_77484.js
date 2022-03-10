// 2021 Dev-Matching: 웹 백엔드 개발자

function solution(lottos, win_nums) {
  let correctCount = 0;
  let zeroCount = 0;

  for (let i = 0; i < lottos.length; i++) {
    if (lottos[i] === 0) {
      correctCount++;
      zeroCount++;
    }

    for (let j = 0; j < win_nums.length; j++) {
      if (lottos[i] === win_nums[j]) {
        correctCount++;
      }
    }
  }

  const best = correctCount;
  const worst = correctCount - zeroCount;
  console.log(best, worst);

  return [getRank(best), getRank(worst)];
}

const getRank = (count) => {
  if (count === 6) {
    return 1;
  }
  if (count === 5) {
    return 2;
  }
  if (count === 4) {
    return 3;
  }
  if (count === 3) {
    return 4;
  }
  if (count === 2) {
    return 5;
  }

  return 6;
};

// 베스트 풀이
function solution(lottos, win_nums) {
  const rank = [6, 6, 5, 4, 3, 2, 1];

  let minCount = lottos.filter((v) => win_nums.includes(v)).length;
  let zeroCount = lottos.filter((v) => !v).length;

  const maxCount = minCount + zeroCount;

  return [rank[maxCount], rank[minCount]];
}
