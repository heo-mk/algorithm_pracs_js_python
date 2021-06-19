# code for converting korean to number
def korean2number(string):
    count_dict = {"일":1,"이":2,"삼":3,"사":4,"오":5,"육":6,"칠":7,"팔":8,"구":9,"십":10,"백":100,"천":1000,"만":10**4,"억":10**8,"조":10**12,"경":10**16}
    a_list = ["일","이","삼","사","오","육","칠","팔","구"]
    b_list = ["십","백","천"]
    c_list = ["만","억","조","경"]

    if string == "영":
        return 0
    else:
        data = list(string)
        subtotal = 0
        total = 0
        a = 0
        for i in range(len(data)):
            count = count_dict.get(data[i])            
            if data[i] in a_list:
                a = count
            if data[i] in b_list:
                b = count
                if a == 0:
                    a = 1
                if data[i] == data[-1] == "천" and total >= 10**8:
                    subtotal = a * b * 10000
                else:
                    subtotal += a * b
                a = 0
            if data[i] in c_list:
                c = count
                if subtotal == 0 and a == 0:
                    if c == "만":
                        a = 1
                    else:
                        return False
                if subtotal == 0:
                    total += a * c
                    a = 0
                else:
                    total += (subtotal + a) * c
                    subtotal = 0
                    a = 0

        total = total + subtotal + a

    return total



# 만 단위 자릿수
tenThousandPos = 4
# 억 단위 자릿수
hundredMillionPos = 9
# 조 단위 자릿수
jo = 13
# 경 단위 자릿수
gyeong = 17

txtDigit = ['', '십', '백', '천', '만', '억', '조', '경']
txtNumber = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
txtPoint = '쩜 '

# Part1 : code for converting number to korean.
def digit2txt(strNum):
    resultStr = ''
    digitCount = 0
    print(strNum)
    #자릿수 카운트
    for ch in strNum:
        # ',' 무시
        if ch == ',':
            continue
        #소숫점 까지
        elif ch == '.':
            break
        digitCount = digitCount + 1


    digitCount = digitCount-1
    index = 0

    while True:
        notShowDigit = False
        ch = strNum[index]
        #print(str(index) + ' ' + ch + ' ' +str(digitCount))
        # ',' 무시
        if ch == ',':
            index = index + 1
            if index >= len(strNum):
                break;
            continue

        if ch == '.':
            resultStr = resultStr + txtPoint
        else:
            #자릿수가 2자리이고 1이면 '일'은 표시 안함.
            # 단 '만' '억'에서는 표시 함
            if(digitCount > 1) and (digitCount != hundredMillionPos) and (digitCount != jo) and (digitCount != gyeong) and int(ch) == 1:
                resultStr = resultStr + ''
            elif int(ch) == 0:
                resultStr = resultStr + ''
                # 단 '만' '억'에서는 표시 함
                if (digitCount != hundredMillionPos) and (digitCount != jo) and (digitCount != gyeong):
                    notShowDigit = True
            else:
                resultStr = resultStr + txtNumber[int(ch)]


        # 1억 이상
        if digitCount > hundredMillionPos:
            if not notShowDigit:
                resultStr = resultStr + txtDigit[digitCount-hundredMillionPos]
        # 1만 이상
        elif digitCount > tenThousandPos:
            if not notShowDigit:
                resultStr = resultStr + txtDigit[digitCount-tenThousandPos]
        else:
            if not notShowDigit:
                resultStr = resultStr + txtDigit[digitCount]

        if digitCount <= 0:
            digitCount = 0
        else:
            digitCount = digitCount - 1
        index = index + 1
        if index >= len(strNum):
            break;
    print(resultStr)

# Part2 : code for converting number to korean .
def number2korean(data):
    for i in range(len(data)):
        num_sum = korean2number(data[i][0]) + korean2number(data[i][1])
        num_list = list(str(num_sum))
        print(digit2txt(num_list))

# test case
DATA = [
    ['오백삼십조칠천팔백구십만천오백삼십구', '삼조사천이만삼천구'],
    ['육십사억삼천십팔만칠천육백구', '사십삼'],
    ['구백육십조칠천억팔천백삼십이만칠천일', '사십삼조오천이백억육천구백십만일'],
    ['이천구백육십조천오백칠십만삼천구백구십', '삼천사백오십조일억이천만육백사십삼'],
    ['사십오억삼천육십만오백구십', '칠십억천이백삼십오만칠천구십이'],
    ['천백십일', '구천오백구십구'],
    ['오억사천', '백십일'],
    ['만오천사백삼십', '십구만삼천오백'],
    ['일조', '삼'],
    ['일억', '만'],
]

# test case result
number2korean(DATA)