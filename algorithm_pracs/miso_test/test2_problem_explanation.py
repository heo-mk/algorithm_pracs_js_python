Test #2
Write a command-line program that prints out the sum of two non-negative integers given as input arguments. Input arguments are UTF-8 encoded Korean characters that represent the non-negative integers only listed as '삼십사' and '십백천만억조', and also your program's output should also be non-negative integers written in the Korean Numbering System encoded with UTF-8. The less you use ifs, the higher you will be scored. Google the Korean Numbering System if you are not familiar with it.
Your program will be tested by the following Python code:


import sys
import subprocess

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
for pair in DATA:
  a, b = pair
  print(a, '+', b, '=', subprocess.check_output([sys.argv[1], sys.argv[2], a, b], encoding='utf-8').strip())
      
Your program is supposed to print to stdout following:


오백삼십삼조일억천팔백구십이만사천오백사십팔
육십사억삼천십팔만칠천육백오십이
천사조이천이백일억오천사십이만칠천이
육천사백십조일억삼천오백칠십만사천육백삼십삼
백십오억사천이백구십오만칠천육백팔십이
만칠백십
오억사천백십일
이십만팔천구백삼십
일조삼
일억일만
      
Do not print out anything but the result string.