const array1 = ['a', 'b', 'c'];
const array2 = ['d', 'd', 'f'];
const array3 = array1.concat(array2);
const array4 = array2.concat(array2);

console.log(array3);
console.log(array4);

array2.concat(array1);
console.log(array2);

const array5 = array1.concat(array1, array2);
console.log(array5);