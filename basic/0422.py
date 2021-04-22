print("섭씨온도 입력하세요.")
temperature = input()
print("화씨온도 : ", (float(temperature) * 1.8) + 32)

# 나이 게산기

def calculateAge(realAge):
    if (realAge >= 20 and realAge <= 26):
        return "대학생"
    elif (realAge >= 17 and realAge < 20):
        return "고등학생"
    elif (realAge >= 14 and realAge < 17):
        return "중학생"
    elif (realAge >= 8 and realAge < 14):
        return "초등학생"
    else:
        return "학생이 아닙니다."


year = int(input())
realAge = (2021 - year + 1)
print(calculateAge(realAge))

# 구구단 계산기

print("구구단 몇 단을 계산할까?")
num = int(input())
for i in range(1, 10):
    print(num, "X", i, "=", num*i)

# 역순

sentence = "i love you"
reverse = ''
for char in sentence:
    reverse = char + reverse
print(reverse)

10진수 -> 2진수

decimal = 10
result = ''
while (decimal > 0):
    remainder = decimal % 2
    decimal = decimal //2
    result = str(remainder) + result
print(result)

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

# 연속적인 구구단 계산기

print("구구단 몇 단을 계산할까요(1~9)")
num = int(input())
print("구구단", num, "단을 계산합니다.")
while (num != 0):
    for i in range(1, 10):
        print(num, "X", i, "=", num*i)
    print("구구단 몇 단을 계산할까요(1~9)")
    num = int(input())
else:
    print("프로그램을 종료합니다.")

# 평균 구하기

# korea = [49, 80, 20, 100, 80]
# math = [43, 60, 85, 30, 90]
# english = [49, 82, 48, 50, 100]
# total = [korea, math, english]
# print(total)
#
# sum = 0
# cnt = 0
# totalSum = 0
#
# for i in range(0, len(total[0])):
#     for j in range(0, len(total)):
#         sum += total[j][i]
#     if (cnt == 0):
#         print("A 학생의 총점 = ", sum)
#         print("A 학생의 평균 = ", sum // len(total))
#     elif (cnt == 1):
#         print("B 학생의 총점 = ", sum)
#         print("B 학생의 평균 = ", sum // len(total))
#     elif (cnt == 2):
#         print("C 학생의 총점 = ", sum)
#         print("C 학생의 평균 = ", sum // len(total))
#     elif (cnt == 2):
#         print("D 학생의 총점 = ", sum)
#         print("D 학생의 평균 = ", sum // len(total))
#     else:
#         print("E 학생의 총점 = ", sum)
#         print("E 학생의 평균 = ", sum // len(total))
#     totalSum += sum
#     sum = 0
#     cnt += 1
#
# print("학생들 총 점수 = ", totalSum)
# print("학생들 총 평균 = ", totalSum // (len(total[0]) * len(total)))

kor = [49, 80, 20, 100, 80]
math = [43, 60, 85, 30, 90]
eng = [49, 82, 48, 50, 100]
midterm = [kor, math, eng]
print(midterm)

studentTotalScore = [0, 0, 0, 0, 0]
index = 0
for subject in midterm:
    for score in subject:
        studentTotalScore[index] += score
        index += 1
    index = 0

else:
    a, b, c, d, e = studentTotalScore
    studentTotalAverage = [a/len(midterm), b/len(midterm), c/len(midterm), d/len(midterm), e/len(midterm)]
    print("학생들의 평균 점수는?")
    print(studentTotalAverage)
    print("가장 높은 평균 점수는?")
    max = max(studentTotalAverage)
    print(max)

# max = 0
# sum = 0
# i = 0
# index = 0
#
# for totalScore in studentTotalScore:
#     if (totalScore > max):
#         max = totalScore
#         index = i
#
#     avg = totalScore / len(midterm)
#     sum += avg
#
#     print("총점 = ", totalScore)
#     print("평균 = ", avg)
#     i += 1
#
# print("전체 평균 = ", sum / len(midterm[0]))
# print("가장 점수가 높은 사람 = ", (index+1), "번째 사람")
# print("가장 점수가 높은 사람의 평균 = ", studentTotalScore[index] / len(midterm))
