# 함수의 실행 순서

def calculate_rectangle_area(x, y):
    return x * y

rectangle_x = 10
rectangle_y = 20
print("사각형 x의 길이 : ", rectangle_x)
print("사각형 y의 길이 : ", rectangle_y)


print("사각형의 넓이 : ", calculate_rectangle_area(rectangle_x, rectangle_y))


# 함수 기초

def f(x):
    return 2 * x + 7
def g(x):
    return x ** 2

x = 2
print(f(x) + g(x) + f(g(x)) + g(f(x)))

def f(x):
    return 2 * x + 7

print(f(2))


# 함수 형태

def a_rectangel_area():
    print(5 * 7)
def b_rectangle_area(x, y):
    print(x * y)
def c_rectangle_area():
    return(5 * 7)
def d_rectangle_area(x, y):
    return(x * y)

a_rectangel_area()
b_rectangle_area(5, 7)
print(c_rectangle_area())
print(d_rectangle_area(5, 7))


# 함수 심화

def f(x):
    y = x
    x = 5
    return y * y

x = 3
print(f(x))
print(x)


# 함수의 호출 방식

def spam(eggs):
    eggs.append(1)
    eggs = [2, 3]
    return eggs

ham = [0]
eggs = spam(ham)
print(ham) # [0, 1]
print(eggs) # [2, 3]

# 변수의 사용 범위

# def test(t):
#     print(x)
#     t = 20
#     print("In Function : ", t)
#
# x = 10
# test(x)
# print("In Main : ", x)
# print("In Main : ", t) # 컴파일 에러


# 변수의 사용 범위

def f():
    s = "I love London!"
    print(s)

s = "I love Paris"
f()
print(s)


# global_variable.py
def f():
    global s
    s = "I love London!"
    print(s)

s = "I love Paris!"
f()
print(s)

# I love London!
# I love London!


# scoping_rule

def calculate(x, y):
    total = x + y
    print("In Function")
    return total

a = 5
b = 7
total = 0
print("In Program - 1")
print("a : ", str(a), "b : ", str(b), "a + b : ", str(a + b))

sum = calculate(a, b)
print("After Calculation")
print("Total : ", str(total), "sum : ", str(sum))


# factorial

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(int(input("Input Number for Factorial Calculation : "))))


# keyword

def print_something(my_name, your_name):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_something("Sungchul", "TEAMLAB")
print_something(your_name = "TEAMLAB", my_name = "Sungchul")


# default.py

def print_something_2(my_name, your_name = "TEAMLAB"):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_something_2("Sungchul", "TEAMLAB")
print_something_2("sungchul")


# asterisk1.py

def asterisk1_test(a, b, *args):
    return a + b + sum(args)

print(asterisk1_test(1, 2, 3, 4, 5))


# asterisk2_py

def asterisk2_test(a, b, *args):
    print(args)

print(asterisk2_test(1, 2, 3, 4, 5))

# (3, 4, 5)
# None


# asterisk3.py

def asterisk3_test(*args):
    x, y, *z = args
    return x, y, z

print(asterisk3_test(3, 4, 5, 10, 20))

# (3, 4, [5, 10, 20])

# test_flake.py

lL0O = "123"
for i in 10:
    print("hello")

# kwargs.py
def kwargs_test(**kwargs):
    print(kwargs)
    print("first value is {first}.".format(**kwargs))
    print("second value is {second}".format(**kwargs))
    print("third value is {third}".format(**kwargs))

kwargs_test(first = 2, second = 4, third = 5)


# hello1.py
def print_hello():
    print("hello world")
    print("hello teamlab")
a = 5
if (a > 3):
    print_hello()
if (a > 4):
    print_hello()
if (a > 5):
    print_hello()

# math2.py
import math

def get_result(a, b, c):
    values = []
    values.append((-b + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
    values.append((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
    return values

print(get_result(1, -2, 1))

import sys
print(sys.getsizeof("a"), sys.getsizeof("ab"), sys.getsizeof("abc"))
# String -> 50개의 공간을 비워 놓고 하나씩 채우기 때문에 50, 51, 52 라고 출력된다.

f = open("C:\\Users\\user\\atom-workspace\\basic\\today.txt", 'r')
today_lyrics = f.readlines()
f.close()
print(today_lyrics)

contents = ""
for line in today_lyrics:
    print(line.strip() + "\n")
    contents = contents + line.strip() + "\n"

n_of_today = contents.upper().count("TODAY")
print("Number of a Word 'Today'", n_of_today)

# formatting.py
print(1, 2, 3)
print("a" + " " + "b" + " " + "c")
print("%d %d %d" % (1, 2, 3))
print("{} {} {}".format("a", "b", "c"))
print("%s %s %s" % (1, 2, 3))

print("I eat %d apples" % 3)
print("I eat %s apples" % "five")

number = 3
day = "three"
print("I ate %d apples. I was sick for %s days." % (number, day))

print("I am {0} years old".format(20))

age = 40
name = "Sungchul Choi"
print("I am {0} years old.".format(age))
print("My name is {0} and {1} years old.".format(name, age))
print("Product : {0}, Price per unit : {1:.2f}.".format("Apple", 5.243))

print("%10.3f" % 5.9434343)
print("%-10.3f" % 5.94343)

print("{0:>10s}".format("Apple"))
print("{0:<10s}".format("Apple"))

# 모듈

from collections import deque

deque_list = deque()
for i in range(6):
    deque_list.append(i)

print(deque_list)
deque_list.pop()
deque_list.pop()

d = {}
d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

for k, v in d.items():
    print(k, v)

from collections import OrderedDict

d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 500
d['l'] = 300

for k, v in d.items():
    print(k, v)


def sort_by_key(t):
    return t[0]


from collections import OrderedDict


d = dict()
d['x'] = 100
d['y'] = 200
d['z'] = 500
d['l'] = 300

for k, v in OrderedDict(sorted(d.items(), key=sort_by_key)).items():
    print(k, v)

from collections import Counter

c = Counter(cats=4, dogs=8)
print(c)
print(list(c.elements()))

from collections import Counter

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)
print(c+d)
print(c)
print(d)
print(c & d)
print(c | d)

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p)
print(p.x, p.y)
print(p[0] + p[1])


# 텍스트 마이닝 프로그램
from collections import defaultdict
from collections import OrderedDict

text = """A press release is the quickest and easiest way to get free publicity.
If well written, a press release can result in multiple published articles
about your firm and its products. And that can mean new prospects contacting
you asking you to sell to them. ...""".lower().split()

word_count = defaultdict(lambda: 0)
for word in text:
    word_count[word] += 1

for k, v in OrderedDict(sorted(word_count.items(), key=lambda t: t[1], reverse=True)).items():
    print(k, v)
