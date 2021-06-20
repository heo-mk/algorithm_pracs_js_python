const template = `템플릿 리터럴은 '작은 따옴표'와 "큰 따옴표"를 혼용할 수 있다`;
console.log(template);

const template1 = `<ul class="nav-items>
  <li><a href="#home">Home</a></li>
  <li><a href="#news">News</a></li>
  <li><a href="#contact">Contact</a></li>
  <li><a href="#about">About</a></li>
</ul>`

console.log(template1);

const first = 'Ung-mo';
const last = "lee";
console.log(`My name is ${first} ${last}.`);

console.log(`1 + 1 = ${1 + 1}`);

const count = '3';
const teacher = "스승";

const tt1 = (str, ...args) => {
  console.log(str);
  console.log(args);
};

tt1`${count}사람이 함께 길을 가면 그 중 반드시 나의 ${teacher}이 있다`;
