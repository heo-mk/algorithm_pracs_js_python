function scope() {
  const a = 0;
  let b = 0;
  var c = 0; //

  if (a === 0) {
    const a = 1;
    let b = 1;
    var c = 1;
    console.log(a, b, c);
  }

  console.log(a, b, c);
}

scope();

let array = [1,2,3,4,5];
let new_array = [...array];
console.log(new_array);

let info = {name: "mean0", id:0};
let is_me = info.name === "mean0" ? true : false; //
console.log(is_me);

const array_num = [0, 1, 2, 3, 4, 5];
const new_array_num = array_num.map((array_item) => {
  return array_item + 1;
})
console.log(new_array_num);
console.log(array_num);

const new_array_filter = array_num.filter((array_item) => {
  return array_item > 3;
});
console.log(new_array_filter);

const array_num01 = [0, 1, 2, 3];
const array_num02 = [3, 4, 5];

const merge = array_num01.concat(array_num02);
console.log(merge);

const merge2 = [...new Set([...array_num01, ...array_num02])];
console.log(merge2);

const my_name = "mean0";
const my_name_array = Array.from(my_name);
console.log(my_name, array);

const text_array = Array.from(my_name_array)