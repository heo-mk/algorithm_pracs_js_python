function solution(money, cost) {
  let arr = [];
  let sum = 0;

  for (let i = 0; i < cost.length; i++) {
    sum = cost[i];
    for (let j = i; j < cost.length; j++) {
      if (j === i && sum > money) {
        arr.push(0);
        break
      }
      if (i === cost.length-1 && sum <= money) {
        arr.push(1);
      }
      if (i === cost.length-1 && sum > money) {
        arr.push(0)
      }
      if (j !== i && sum <= money) {
        sum += cost[j];
        if (sum > money) {
          arr.push(j - i)
          break
        }
        if (sum <= money && j == cost.length - 1) {
          arr.push(cost.length - i)
        }
      }; 
    };
  };

  console.log(arr);
  let max_length = arr.reduce((prev, curr) => {
    return prev > curr ? prev : curr;
  });
  console.log(max_length);
  return max_length;
};

console.log(solution(420, [0, 900, 0, 200, 150, 0, 30, 50]));
console.log(solution(100, [245, 317, 151, 192]));