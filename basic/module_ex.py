import fah_converter as fah

print("enter a celsius value : ")
celsius = float(input())
fahrenheit = fah.convert_c_to_f(celsius)
print("That is ", fahrenheit, "degrees fahrenheit")


# 특정 메소드만 import

from fah_converter import convert_c_to_f

print("enter a celsius value : ")
celsius = float(input())
fahrenheit = convert_c_to_f(celsius)
print("That is ", fahrenheit, "degrees fahrenheit")


# 모든 메소드 import

from fah_converter import *
print(convert_c_to_f(30))
