var a = 10;
function scope1() {
  a = 20;
  console.log(a);
}

scope1();
console.log(a);

var b = 10;
function scope2() {
  var b = 20;
  console.log(b);
};
scope2();
console.log(b);