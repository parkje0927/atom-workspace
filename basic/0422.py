# print("섭씨온도 입력하세요.")
# temperature = input()
# print("화씨온도 : ", (float(temperature) * 1.8) + 32)

# 나이 게산기

# def calculateAge(realAge):
#     if (realAge >= 20 and realAge <= 26):
#         return "대학생"
#     elif (realAge >= 17 and realAge < 20):
#         return "고등학생"
#     elif (realAge >= 14 and realAge < 17):
#         return "중학생"
#     elif (realAge >= 8 and realAge < 14):
#         return "초등학생"
#     else:
#         return "학생이 아닙니다."
#
#
# year = int(input())
# realAge = (2021 - year + 1)
# print(calculateAge(realAge))

# 구구단 계산기

# print("구구단 몇 단을 계산할까?")
# num = int(input())
# for i in range(1, 10):
#     print(num, "X", i, "=", num*i)

# 역순

# sentence = "i love you"
# reverse = ''
# for char in sentence:
#     reverse = char + reverse
# print(reverse)

# 10진수 -> 2진수

# decimal = 10
# result = ''
# while (decimal > 0):
#     remainder = decimal % 2
#     decimal = decimal //2
#     result = str(remainder) + result
# print(result)

# 숫자 찾기 게임

import random
guess = random.randint(1, 100)
print("숫자를 맞혀보세요. (1 ~ 100)")
usersInput = int(input())
while (usersInput is not guess):
    if (usersInput > guess):
        print("숫자가 너무 큽니다.")
    else:
        print("숫자가 너무 작습니다.")
    usersInput = int(input())
else:
    print("정답입니다.", "입력한 숫자는", usersInput, "입니다.")    
