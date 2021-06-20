var a = [1,2,3,4,5,6,7,8,9]
result = a.reduce((acc, cur, i) => {
  console.log(acc, cur, i);
  return acc + cur;
}, 10);
console.log();

result2 = a.reduceRight((acc, cur, i) => {
  console.log(acc, cur, i);
  return acc + cur;
}, 10);
console.log();

var b = [1,2,3,4,5,6,7]
result3 = b.reduce((acc, cur, i) => {
    acc.push(cur %2 ? '홀수':'짝수');
  return acc;
}, []);
console.log(result3);

result4 = b.reduce((acc, cur, i) => {
    if (cur%2) {
      acc.push('홀수')
    }
  return acc;  
},[])
console.log(result4);

const numbers = [1,2,3,4,5,6,7,8,9,10];

const sum1 = numbers.reduce((acc, cur) => acc + cur);
console.log(sum1);

// reduce 함수에는 콜백, 초기값만 들어간다.
function sumReducer(acc, cur) {
  return acc + cur;
}
const sum2 = numbers.reduce(sumReducer, 100);
console.log(sum2);

const friends = [
  {
    name: '양주진',
    age: 32,
    job: '코인러',
    married: false,
  },
  {
    name: '오영제',
    age: 32,
    job: '랩퍼',
    married: false,
  },
  {
    name: '서준형',
    age: 32,
    job: '2년차 유부남',
    married: true,
  }
];

const ageSum = friends.reduce((acc, curObj) => {
  return acc + curObj.age;
}, 0)
console.log('친구들 나이 합', ageSum);

const users1 = [
  { name: 'John', age: 34 },
  { name: 'Mehdi', age: 19 },
  { name: 'Alex', age: 10 }
];

const sumOfAges = users1.reduce((sum, user) => sum + user.age, 0);
console.log(sumOfAges);

const users2 = [
  { name: 'John', age: 34 },
  { name: 'Mehdi', age: 19 },
  { name: 'Alex', age: 10 }
];

const userObj = users2.reduce((obj, user, i) => {
  obj[user.name] = user.age;
  console.log(obj, user, i);
  return obj;
}, {});
console.log(userObj);