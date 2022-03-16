function solution(strings, n) {
  strings = strings.sort();
  const sorted = strings.map((v, idx) => ({ val: v, v: v[n] }));

  return sorted
    .sort((a, b) => {
      const aV = a.v.toLowerCase();
      const bV = b.v.toLowerCase();

      if (aV < bV) return -1;
      if (aV > bV) return 1;
      return 0;
    })
    .map((v) => v.val);
}
