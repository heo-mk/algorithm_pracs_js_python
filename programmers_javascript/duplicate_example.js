function duplicate(arr) {
  return arr.concat(arr);
}

console.log(duplicate([1,2,3,4,5]))

for (let i = 1; i <= 100; i++) {
  let f = i % 3 == 0,
    b = i % 5 == 0 
    console.log(f ? (b ? 'FizzBuzz' : 'Fizz') : b ? 'buzz' : i)
};

let temperature = 20
while (temperature < 25) {
  console.log(`${temperature}도 정도면 적당한 온도입니다`)
  temperature++
}

let foo = ["one", "two", "three"];
let [one, two, three] = foo;
console.log(one);
console.log(two);
console.log(three);

var a, b;

[a , b] = [1, 2];
console.log(a);
console.log(b);

function f() {
  return [1, 2, 3];
}

let a1 = 31;
let a2 = String(a1);
console.log(a2);

let a3 = a1.toString();
console.log(a3);

console.log(typeof a1);
console.log(typeof a2);
console.log(typeof a3);

let words = ['banana', 'apple', 'caramel']
words.sort()
console.log(words);

let words2 = [31, 111, 222, 444]
words2.sort()
console.log(words2)

let words3 = [31, 111, 222, 444]
words3.sort((a, b) => {
  return a - b
})
console.log(words3);