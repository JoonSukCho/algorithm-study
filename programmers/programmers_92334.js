function solution(id_list, report, k) {
  const uniqueReport = [...new Set(report)];
  var answer = id_list.map(() => 0);

  const rObj = {};

  id_list.forEach((v) => (rObj[v] = []));

  uniqueReport.map((v) => {
    const [singo, fisingo] = v.split(" ");
    rObj[fisingo].push(singo);
  });

  for (const key in rObj) {
    if (rObj[key].length >= k) {
      rObj[key].map((user) => {
        answer[id_list.indexOf(user)] += 1;
      });
    }
  }

  return answer;
}
