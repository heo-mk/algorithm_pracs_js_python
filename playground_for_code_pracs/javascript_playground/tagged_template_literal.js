let person = 'lee';
let age = 28;

let tag = function(strings, personExp, ageExp) {
  let str0 = strings[0];
  let str1 = strings[1];
  console.log("str0 : " + str0);
  console.log("str1 : " + str1);

  let ageStr;
  if (ageExp > 99) ageStr = 'centenaian';
  else ageStr = 'youngster';

  return str0 + personExp + str1 + ageStr;
};
let output = tag`that ${person} is a ${age}`;
console.log(output);
