function getClosure() {
  var text = 'variable 1';
  return function() {
    return  text;
  };
}

var closure = getClosure();
console.log(closure());
console.log();

var base = 'hello, ';
function sayHelloTo(name) {
  var text = base + name;
  return function() {
    console.log(text);
  };
}

var hello1 = sayHelloTo('과케미');
var hello2 = sayHelloTo('이즌');
var hello3 = sayHelloTo('양파');
hello1();
hello2();
hello3();
console.log();

function Hello(name) {
  this._name = name;
}

Hello.prototype.say = function () {
  console.log('Hello, ' + this._name);
}

var Hello4 = new Hello('감자');
var Hello5 = new Hello('고추');
var Hello6 = new Hello('배추');

Hello4.say();
Hello5.say();
Hello6.say();
Hello4._name = 'anonymous';
Hello4.say();