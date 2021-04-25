for i in range(10):
    try:
        print(10 / i)
    except ZeroDivisionError as e:
        print(e)
        print("Not divided by 0")
    else:
        print(10 / i)


# try:
#     예외가 발생 가능 코드
# except 예외 타입:
#     예외 발생 시 실행되는 코드
# else:
#     예외가 발생하지 않을 때 실행되는 코드


try:
    for i in range(1, 10):
        result = 10 // i
        print(result)

except ZeroDivisionError:
    print("Not divided by 0")

finally:
    print("종료되었다.")


# try:
#     예외가 발생 가능 코드
# except 예외 타입:
#     예외 발생 시 실행되는 코드
# finally:
#     예외 발생 여부와 상관없이 실행되는 코드

# raise 예외 타입(예외 정보) : 예외를 발생시키는 코드

# assert 예외 조건

# def get_binary_number(decimal_number):
#     assert isinstance(decimal_number, int)
#     return bin(decimal_number)
#
#
# print(get_binary_number(10))
# print(get_binary_number("10"))


# 파일

with open("C:\\Users\\user\\atom-workspace\\basic\\dream.txt", "r") as my_file:
    contents_list = my_file.readlines()
    print(type(contents_list))
    print(contents_list)


with open("C:\\Users\\user\\atom-workspace\\basic\\dream.txt", "r") as my_file:
    i = 0
    while 1:
        line = my_file.readline()
        if not line:
            break
        print(str(i) + " === " + line.replace("\n", ""))
        i += 1

with open("C:\\Users\\user\\atom-workspace\\basic\\dream.txt", "r") as my_file:
    contents = my_file.read()
    word_list = contents.split(" ")
    line_list = contents.split("\n")

print("총 글자의 수 : ", len(contents))
print("총 단어의 수 : ", len(word_list))
print("총 줄의 수 : ", len(line_list))


f = open("count_log.txt", "w", encoding='utf8')
for i in range(1, 11):
    data = "%d번째 줄이다.\n % i"
    f.write(data)
f.close()


with open("count_log.txt", 'a', encoding="utf8") as f:
    for i in range(1, 11):
        data = "%d 번째 줄이다. \n" % i
        f.write(data)



import os

if not os.path.isdir("log"):
    os.mkdir("log")

if not os.path.exists("log/count_log.txt"):
    f = open("log/count_log.txt", 'w', encoding="utf8")
    f.write("기록이 시작된다.\n")
    f.close()

with open("log/count_log.txt", "a", encoding="utf8") as f:
    import random, datetime
    for i in range(1, 11):
        stamp = str(datetime.datetime.now())
        value = random.random() * 1000000
        log_line = stamp + "\t" + str(value) + "값이 생성되었다.\n"
        f.write(log_line)
