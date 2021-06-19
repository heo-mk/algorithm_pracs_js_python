function delay() {
  for (var i = 0; i < 100000 ; i++);
}

function foo() {
  delay();
  bar();
  console.log('foo!'); 
}

function bar() {
  delay();
  console.log('bar!');
}

function baz() {
  console.log('baz!');
}

setTimeout(foo, 10);
setTimeout(bar, 10);
setTimeout(baz, 10);

setTimeout(function() {
  console.log('A');
}, 0);
// console.log('B');
Promise.resolve().then(function() {
  console.log('B');
}).then(function() {
  console.log('C');
});

