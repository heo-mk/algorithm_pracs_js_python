var name = "온선희";
var job = "마케터";
var hobby = "게임하기";

console.log(
  "안녕하세요, 저의 이름은 \"" + name + "\"입니다.\n " +
  "직업은 \"" + job + "\"이구요, \n" + 
  "취미는 \"" + hobby + "입니다. \n"
);

console.log(
`안녕하세요, 저의 이름은 ${name}입니다.
직업은 ${job}이구요,
취미는 ${hobby}입니다.`
);

console.log(`
${1 + 1}`
)

let name2 = `Jae Hong rke`;
let intro = 
`
Hello~ ${
  `my name is ${name2}`
}`.trim();
console.log(intro);

let hw = 
`
hello
world!
`.trim();
console.log(hw);
console.log(hw.length);
console.log();

// tagged template
let hw2 = tag`hello world`;

var a = 5;
var b = 10;

function tag(strings, ...values) {
  // console.log(strings[0]); // "hello "
  // console.log(strings[1]); // " world "
  // console.log(strings[2]); // "!"
  // console.log(values[0]); // 15
  // console.log(values[1]); // 50

  strings.forEach(function(v, i) {
    console.log(`str${i}: ${v}`);
  });
  values.forEach(function(v, i) {
    console.log(`values${i}: ${v}`);
  });

  return "Banziga!";
}

tag`Hello ${a + b}${a/b}${a-b} world ${a * b}!`;
