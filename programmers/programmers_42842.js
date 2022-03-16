function solution(brown, yellow) {
  var answer = [];
  let allTiles = brown + yellow;

  // 모든 타일 갯수의 약수를 구한다.
  let idx = 1;
  const yaksu = [];
  while (idx <= allTiles) {
    if (allTiles % idx === 0) {
      yaksu.push(idx);
    }

    idx++;
  }

  // 약수로 나올 수 있는 카펫의 크기를 만들면서
  // yellow 갯수를 조건으로 조건 만족시 answer 할당
  for (let i = 0; i < yaksu.length / 2; i++) {
    let garo = yaksu[yaksu.length - 1 - i];
    let sero = yaksu[i];

    if ((garo - 2) * (sero - 2) === yellow) {
      answer = [garo, sero];
    }
  }

  return answer;
}
