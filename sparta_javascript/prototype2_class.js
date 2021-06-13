function Item(name) {
  this.apple = name;
  return name;
}

console.log(Item.prototype.constructor.apple('apple')); // output
console.log(apple.name);

class Item2 {
  constructor(name) {
    this.apple = name;
    return name;
  }
}

console.log(Item2.prototype.constructor.apple('apple'));