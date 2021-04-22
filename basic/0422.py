# print("섭씨온도 입력하세요.")
# temperature = input()
# print("화씨온도 : ", (float(temperature) * 1.8) + 32)

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
