function solution(numbers) {
  let answer = numbers.map(c => c + '').sort((a, b) => (b+a) - (a+b).join(''));
  return answer[0] === "0" ? '0' : answer;
}

console.log(solution([[6, 10, 2]]));

// new way
function solution2(numbers) {
  let answer = '';
  numbers.sort((a,b) => {
    return Number((String(b) + String(a)) - Number(String(a) + String(b)));
  })

  numbers.forEach(element => {
    answer += element + ""
  });

  if (answer[0] === "0") {
    return '0';
  }

  return answer;
};

console.log(solution2([[6, 10, 2]]));