class Cat {
  constructor(name) {
    this.name = name;
  }

  showName() {
    return this.name
  }
}

class MyCat extends Cat {
  constructor(name, age) {
    super(name, age);
    this.age = age;
  }

  showName() {
    return '내 고양이 이름은' + super.showName() + '입니다.';
  }

  showAge() {
    console.log('내 고양이는' + this.age + '살 입니다!')
  }
}

let my_cat = new MyCat('perl', 4);
my_cat.showName();
my_cat.showAge();
