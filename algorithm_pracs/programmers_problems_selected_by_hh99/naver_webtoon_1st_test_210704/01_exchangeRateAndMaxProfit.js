function solution(k, rates) {
  let max_rate = rates.reduce((prev, curr) => {
    return prev > curr ? prev : curr;
  });
  console.log(max_rate);
  let dollars = 0;

  if (k >= max_rate) {
    return k;
  } else {
    for (i = 0; i < rates.length-1; i++) {
      // if (k >= rates[i] && dollars === 0) {
      // 원화를 팔고 달러를 살 때
      if (k >= rates[i]) {
        for (let j = i; j < rates.length-1; j++) {
          if (rates[j+1] - rates[j] > 0) {
            k -= rates[j];
            dollars += 1;
            break;
          }
        }
      }
      // 달러를 팔고 원화를 살 때
      // if (k < rates[i] && dollars !== 0) {
      if (dollars !== 0) {
        for (let j = i; j < rates.length-1; j++) {
          if (rates[j] > rates[j-1] && rates[j+1] - rates[j] < 0) {
            dollars -= 1;
            k += rates[i]
          }
        };
      }
    }
    // if (i = rates.length-1 && dollars !== 0) {
    //   dollars -= 1;
    //   k += rates[i]
    // };
  }
  // console.log(dollars);
  // console.log(k);

  return k;
};

console.log(solution(1000, [1200, 1000, 1100, 1200, 900, 1000, 1500, 900, 750, 1100]));
// console.log(solution(1500, [1500, 1400, 1300, 1200]));