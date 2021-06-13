function CreateItem() {};
const NewItem = new CreateItem();

const obj1 = {};
const obj2 = new Object();

const newObj = {};
// const newNewObj = new newObj; // 에러 포인트

function Item() {}
Item.prototype.apple = 1;
Item.prototype.banana = 4;

const FruitStore = new Item();
console.log(FruitStore.apple);

