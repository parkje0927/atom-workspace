# 파이썬 스타일 코드 I

colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)
print(result)

items = 'zero one two three'.split()
print(items)

example = 'python, jqeury, javascript'
example.split(",")
print(example)
a, b, c = example.split(",")
print(a, b, c)

result = ' '.join(colors)
print(result)
result = ', '.join(colors)
print(result)

result = [i for i in range(10)]
print(result)

result = [i for i in range(10) if i % 2 == 0]
print(result)

# else 붙일 경우 조건문이 앞으로 간다.
result = [i if i % 2 == 0 else 10 for i in range(10)]
print(result)

word1 = "hello"
word2 = "world"
result = [i + j for i in word1 for j in word2]
print(result)

result = [i + j for i in word1 for j in word2 if i != j]
print(result)

words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)
for i in stuff:
    print(i)

case1 = ['a', 'b', 'c']
case2 = ['d', 'e', 'a']

# 일차원 리스트 출력
# ['ad', 'ae', 'aa', 'bd', 'be', 'ba', 'cd', 'ce', 'ca']
result = [i + j for i in case1 for j in case2]
print(result)

# 이차원 리스트 출력
# [['ad', 'bd', 'cd'], ['ae', 'be', 'ce'], ['aa', 'ba', 'ca']]
result = [[i + j for i in case1] for j in case2]
print(result)

# 일반적인 반복문 + 리스트
# def scalar_vector_product(scalar, vector):
#     result = []
#     for value in vector:
#         result.append(scalar * value)
#     return result


# iteration_max = 10000
#
# vector = list(range(iteration_max))
# scalar = 2

# for _ in range(iteration_max):
#     scalar_vector_product(scalar, vector)


# iteration_max = 10000

# vector = list(range(iteration_max))
# scalar = 2

# for _ in range(iteration_max):
#     [scalar * value for value in range(iteration_max)]


# enumerate
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# 0 tic
# 1 tac
# 2 toe

alist = ['a1', 'b1', 'c1']
blist = ['a2', 'b2', 'c2']
for a, b in zip(alist, blist):
    print(a, b)
# a1 a2
# b1 b2
# c1 c2

a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)
[print(sum(x)) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))]

alist = ['a1', 'b1', 'c1']
blist = ['a2', 'b2', 'c2']
for i, (a, b) in enumerate(zip(alist, blist)):
    print(i, a, b)


# # 람다
# f = lambda x, y: x + y
# print(f(1, 4))
#
# print((lambda x: x+1)(5))
#
# f = lambda x: x ** 2
# print(f(5))
#
#
# # 맵리듀스
#
# ex = [1, 2, 3, 4, 5]
# f = lambda x: x ** 2
# print(list(map(f, ex)))
#
# temp = [x ** 2 for x in ex]
# print(temp)
#
# ex = [1, 2, 3, 4, 5]
# f = lambda x, y: x + y
# temp = list(map(f, ex, ex))
# print(temp)
#
# temp = list(map(lambda x: x ** 2 if x % 2 == 0 else x, ex))
# print(temp)
# temp = [x ** 2 if x % 2 == 0 else x for x in ex]
# print(temp)
#
#
# from functools import reduce
# print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])) # 15
#
#
# def asterisk_test(a, *args):
#     print(a, args) # 1 (2, 3, 4, 5, 6)
#     print(type(args)) # tuple
#
#
# asterisk_test(1, 2, 3, 4, 5, 6)
#
#
# def asterisk_test(a, **kargs):
#     print(a, kargs) # 1 {'b': 2, 'c': 3, 'd': 4, 'e': 5}
#     print(type(kargs)) # dict
#
# asterisk_test(1, b=2, c=3, d=4, e=5)
#
#
# def asterisk_test(a, args):
#     print(a, *args) # 1 2 3 4 5 6
#     print(type(args)) # tuple
#
# asterisk_test(1, (2, 3, 4, 5, 6))
# # 변수 앞의 별표는 해당 변수를 언패킹한다. 즉 하나의 튜플이 아닌 각각의 변수로 변경
#
#
# a, b, c = ([1, 2], [3, 4], [5, 6])
# print(a, b, c)
# data = ([1, 2], [3, 4], [5, 6])
# print(*data)
#
# for data in zip(*[[1, 2], [3, 4], [5, 6]]):
#     print(data)
#     print(type(data))
#
#
# def asterisk_test(a, b, c, d):
#     print(a, b, c, d)
#
# data = {"b":1, "c":2, "d":3}
# asterisk_test(10, **data)
#
#
#
# # 선형대수학
#
# u = [2, 2]
# v = [2, 3]
# z = [3, 5]
#
# result = [sum(t) for t in zip(u, v, z)]
# print(result)
#
#
# def vector_addition(*args):
#     return [sum(t) for t in zip(*args)]
#
# vector_addition(u, v, z)
# # *args 를 사용하여 여러 개의 변수를 입력 받는 가변 인수로 사용하였다.
# # 그리고 실제 함수에서는 args 에 별표를 붙여 언패킹하였다.
#
# row_vectors = [[2, 2], [2, 3], [3, 5]]
# vector_addition(*row_vectors)

u = [1, 2, 3]
v = [4, 4, 4]
alpha = 2

result = [alpha * sum(t) for t in zip(u, v)]
print(result)

matrix_a = [[3, 6], [4, 5]]
matrix_b = [[5, 8], [6, 7]]
result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]
print(result)

matrix_a = [[1, 1], [1, 1]]
matrix_b = [[1, 1], [1, 1]]
# all(row[0] == value for t in zip(matrix_a, matrix_b) for row in zip(*t) \
# for value in row])

# 행렬의 곱셈은 앞 행렬의 열과 뒤 행렬의 행을 선형 결합한다.
# (2 X 3)(3 X 2) = (2 X 2) 행렬

matrix_a = [[1, 1, 2], [2, 1, 1]]
matrix_b = [[1, 1], [2, 1], [1, 3]]
result = [[sum(a * b for a, b in zip(row_a, column_b)) for column_b \
in zip(*matrix_b)] for row_a in matrix_a]
print(result)
