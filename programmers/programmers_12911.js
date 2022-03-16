function solution(n) {
  var answer = 0;
  let next = n;
  let nOneCount = 0;
  n.toString(2)
    .split("")
    .map((v) => {
      if (v === "1") {
        nOneCount++;
      }
    });

  while (true) {
    let oneCount = 0;
    next++;
    next
      .toString(2)
      .split("")
      .map((v) => {
        if (v === "1") {
          oneCount++;
        }
      });

    if (nOneCount === oneCount) {
      answer = next;
      break;
    }
  }

  return answer;
}
