// forEach()
const arr = [1, 2, 3, 4, 5];
const mulArr = [];

arr.forEach(num => {
  mulArr.push(num*3);
});

console.log(mulArr);

let arr3 = [1,2,3,4,5];
let a = arr3.forEach(function(value) {
  return value;
});
console.log(a);

// map()
const arr2 = [1, 2, 3, 4, 5];
const mulArr2 = arr.map(num => num*3);
console.log(mulArr2);

let arr4 = [1,2,3,4,5];
let b = arr3.map(function(value) {
  return value + 1; 
});
console.log(b);

// reduce()
[0,1,2,3,4].reduce(function(accumulator, currentValue, currentIndex, array){
  return accumulator + currentIndex;
});

let arr5 = [1,2,3,4,5];
let c = arr5.reduce(function(preValue, currentValue) {
  return preValue + currentValue;
});
console.log(c);

const arr6 = [1,2,3,4,5,6];
const reducer = (accumulator, currentValue) => accumulator + currentValue;

// 1 + 2 + 3 + 4 + 5 + 6 
console.log(arr6.reduce(reducer));
// 7 + 1 + 2 + 3 + 4 + 5 + 6
console.log(arr6.reduce(reducer, 7));

let total = [1,2,3,4,5].reduce(
  (acc, curr) => acc + curr,
  0
);
console.log(total);

let total2 = [{quantity:1}, {quantity:2}, {quantity:1}].reduce(
  (acc, curr) => acc + curr.quantity, 0
);
console.log(total2);

let max = [1,2,3,4,5].reduce(
  (max, cur) => Math.max(max, cur), -Infinity
);
console.log(max);

let flattened = [[0,1], [2,3], [4,5]].reduce(
  (acc, cur) => acc.concat(cur), []
);
console.log(Math.max(1,2,3));