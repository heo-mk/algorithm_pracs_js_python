function outer() {
  let name = "gongseungyeon";
  function inner() {
    console.log(`hello ${name}`);
  }

  inner();
  return inner;
}

let greeting = outer();
greeting();