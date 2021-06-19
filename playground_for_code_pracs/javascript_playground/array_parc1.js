const animals = ['강아지', '고양이', '햄스터', '토끼', '고양이'];

let count = 0;
for (let i=0 ; i < animals.length; i++) {
  let animal = animals[i];
  if (animal === "고양이") {
    count += 1;
  }
}
console.log(count);

let count2 = 0;
animals.map((animal) => {
  if (animal === "고양이") {
    count2 += 1;
  }
});
console.log(count);

