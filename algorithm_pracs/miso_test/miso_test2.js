function calculate(data) {
  let calNum = 0;
  calNum += convert_Num(data[0]);
  calNum += convert_Num(data[1]);
  return convert_Kor(calNum);
}
function convert_Num(korNum) {
  const number = {
    영: 0,
    일: 1,
    이: 2,
    삼: 3,
    사: 4,
    오: 5,
    육: 6,
    칠: 7,
    팔: 8,
    구: 9,
  };
  const small_unit = {
    십: 10,
    백: 100,
    천: 1000,
  };
  const big_unit = {
    만: 10000,
    억: 100000000,
    조: 1000000000000,
  };
  let count = 0;
  let unit_count = 0;
  let oneNum = 0;
  for (const i in korNum) {
    if (number[korNum[i]] != undefined) {
      oneNum = number[korNum[i]];
    } else {
      if (small_unit[korNum[i]] != undefined) {
        unit_count += (oneNum != 0 ? oneNum : 1) * small_unit[korNum[i]];
      } else {
        unit_count = unit_count + oneNum;
        count += (unit_count != 0 ? unit_count : 1) * big_unit[korNum[i]];
        unit_count = 0;
      }
      oneNum = 0;
    }
  }
  return count + unit_count + oneNum;
}
function convert_Kor(num) {
  const number = ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"];
  const small_unit = ["", "십", "백", "천"];
  const big_unit = ["", "만", "억", "조"];
  return String(num)
    .split("")
    .reverse()
    .map((element, index, arr) => {
      const cvtIdx = index % 4;
      const unitIdx = Math.ceil(index / 4);
      let korNum = number[element];
      let smallUnit = element == 0 ? "" : small_unit[cvtIdx];
      let bigUnit = cvtIdx == 0 ? big_unit[unitIdx] : "";
      korNum = korNum == "일" && smallUnit != "" ? "" : korNum;
      if (cvtIdx == 0 && index + 4 <= arr.length - 1) {
        let count = 0;
        for (let i = 0; i < 4; i++) {
          if (arr[index + i] == "0") {
            count++;
          }
        }
        bigUnit = count == 4 ? "" : bigUnit;
      }
      if (cvtIdx == 0 && index == arr.length - 1 && bigUnit == "만") {
        korNum = korNum == "일" ? "" : korNum;
      }
      return korNum + smallUnit + bigUnit;
    })
    .reverse()
    .join("");
}
for (const i in data) {
  let convert = calculate(data[i]);
  console.log(convert);
}