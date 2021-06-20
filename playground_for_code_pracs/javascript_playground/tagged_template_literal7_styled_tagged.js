let value = 10;
console.log("음 이렇게 하고 나서 " + value + " 이렇게 더 하기로 써줘야 하는디");
console.log(`음 이렇게 하고 나서 ${value} 이렇게 더 하기로 써줘야 하는디`);

let name = "래쉬";
let age = 22;

function flip(strings, personName, personAge) {
  let str0 = strings[0];
  let str1 = strings[1];
  return personAge + str1 + personName + " " + str0;
}

let input = `Hello, ${name}, you are ${age}`;
let output = flip`Hello, ${name}, you are ${age}`;

console.log(input);
console.log(output);

const name1 = 'John';
const location = 'cheongdo';

const tag = (strs, firstExpr, secondExpr) => {
  return console.log(strs, firstExpr, secondExpr)
};

tag`나는 ${location}에 살고 있는 ${name}이야`

const styled = (strs, ...exprs) => [strs, exprs];

const result = styled`
  background-color: ${({primary}) => (primary ? 'white' : primaryColor)};
  padding: 1rem;
`

console.log(result);