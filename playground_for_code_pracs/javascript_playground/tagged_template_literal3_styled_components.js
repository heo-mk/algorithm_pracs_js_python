const obj = {
  a: 1,
  b: 2, 
  c:3
};

console.log(`${obj}`);

const obj2 = () => {
  return {
    a:1,
    b:2,
    c:3
  }
};
console.log(obj2);

const v1 = "사과";
const v2 = "딸기";
const v3 = "포도";

function getFruits(texts, ...rest) {
  // console.log(texts);
  // console.log(rest);
  return texts.reduce((acc, cur, i) => `${acc}${cur}${rest[i] ? `${rest[i]}` : ''}`, '');
};

getFruits`판매량이 높은 과일로는 ${v1}, ${v2}, ${v3}가 있습니다` 

const styled = {
  p(texts, ...rest) {
    const defaultProps = {
      color1: 'yellow',
      color2: 'orange'
    }
    return texts.reduce((acc, cur, i) => `${acc}${cur}${rest[i] ? `${rest[i](defaultProps)}` : ''}`, '');
  }
}

styled.p`
background: ${props => props.color1};
color: ${props => props.color2}
`
