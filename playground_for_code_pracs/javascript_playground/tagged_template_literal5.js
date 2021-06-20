// var person = 'Mike';
// var age = 28;

// function myTag(strings, personExp, ageExp) {
//   var str0 = strings[0];
//   var str1 = strings[1];

//   var ageStr;
//   if (ageExp > 99) {
//     ageStr = 'centerarian';
//   } else {
//     ageStr = 'youngster';
//   }

//   return str0 + personExp + str1 + ageStr;
// };

// var output = myTag`that ${ person } is a ${ age }`;
// console.log(output);

function getPersonInfo(one, two, three) {
  console.log(one);
  console.log(two);
  console.log(three);
}

const person = 'Lydia';
const age = 21;

getPersonInfo`${person} is ${age} years old`;



