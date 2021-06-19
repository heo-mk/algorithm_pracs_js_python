const superHero = new Map();
superHero.set('Superman', 'Clark Kent');
superHero.set('Batman', 'Bruce Wayne');
superHero.set('Batman', 'Dick Grayson');
superHero.set(NaN, 'Flash');
console.log(superHero.get('Batman'));

const heroList = [
  ['Superman', 'Clark Kent'],
  ['Batman', 'Bruce Wayne'],
  ['Wondeerwoman', 'Diana Prince'],
  ['Greenman', 'Hal Jordan'],
  ['Aquaman', 'Arther Curry'],
  ['Flash', 'Barry Allen'],
  ['Green Arrow', 'Oliver Queen'],
];

let justiceLeague = new Map(heroList);
console.log(justiceLeague);

console.log(superHero.size);
superHero.get('Superman');
superHero.get('Flash');

for (let [key, value] of justiceLeague) {
  console.log(`${key} - ${value}`)
};
console.log();

for (let [key, value] of justiceLeague.entries()) {
  console.log(`${key} - ${value}`)
};

console.log(justiceLeague.size);

console.log(superHero.get(NaN));