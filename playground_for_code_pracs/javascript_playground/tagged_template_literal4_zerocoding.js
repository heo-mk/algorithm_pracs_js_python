// const Title = styled.h1`
//   font-size: 1.5em;
//   text-align: center;
//   color: palevioletred;
// `

const tag = (...args) => console.log(args);
tag`너의 정체가 도대체 뭐니?`;

const a = '정체가';
const b = '뭐니';
tag`너의 ${a} 도대체 ${b}`;

const tag1 = (strs, ...vars) => console.log(strs, vars, strs.raw);
tag1`너의 ${a} 도대체 ${b}`;

const consoleLog = (strs, ...vars) => {
  const string = strs.reduce((prev, cur, i) => prev + strs[i] + (vars[i] || ''), '');
  console.log(string);
  return string;
};

const str = `너의 ${a} 도대체 ${b}`;
console.log(str);
consoleLog`너의 ${a} 도대체 ${b}`;

const engAndNumOnly = (strs, ...vars) => {
  const string = strs.reduce((prev, cur, i) => prev + strs[i] + (vars[i] ? vars[i].replace(/[^A-z0-9]/g, ''): ''), '');
  console.log(string);
  return string;
}

const c = 'English와 한글';
const d = '0-9 and !@#';
engAndNumOnly`Yo! ${c} ${d}`;
