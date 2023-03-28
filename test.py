a = float(input("분수1, 분모: "))
b = float(input("분수1, 분자: "))
c = float(input("분수2, 분모: "))
d = float(input("분수2, 분자: "))

# 통분하기
ac = a*c 
bc = b*c
ad = a*d 

numerator = bc+ad #분자
denominator = ac #분모

# 분모, 분자의 최대공약수 찾기

if numerator >= denominator:
    big_number = numerator
    small_number = denominator
else:
    big_number = denominator
    small_number = numerator

remain = big_number%small_number

while remain !=0:
    big_number = small_number
    small_number = remain
    remain = big_number%small_number

gcd = small_number

# 기약분수 만들기

irreducible_numerator = numerator / gcd
irreducible_denominator = denominator / gcd

# 가분수 정리
if irreducible_numerator >= irreducible_numerator:
    result_numerator = irreducible_numerator % irreducible_denominator
    result_natural_number = irreducible_numerator // irreducible_denominator

if result_natural_number !=0:
    print (result_natural_number, "과", result_numerator, "/", irreducible_denominator)
else:
    print (irreducible_numerator, "/", irreducible_denominator)