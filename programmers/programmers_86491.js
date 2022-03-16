function solution(sizes) {
  var answer = 0;
  const leftSide = [];
  const rightSide = [];

  for (let i = 0; i < sizes.length; i++) {
    if (sizes[i][1] > sizes[i][0]) {
      sizes[i].reverse();
    }
    leftSide.push(sizes[i][0]);
    rightSide.push(sizes[i][1]);
  }

  return Math.max(...leftSide) * Math.max(...rightSide);
}
