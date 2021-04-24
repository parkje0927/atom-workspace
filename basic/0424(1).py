class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self):
        print("저의 이름은", self.name, "이고요, 제 나이는", str(self.age), "살 입니다.")


class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender)
        self.salary = salary
        self.hire_date = hire_date

    def do_work(self):
        print("열심히 일을 한다.")

    def about_me(self):
        super().about_me()
        print("제 급여는", self.salary, "원 이고, 제 입사일은", self.hire_date, "입니다.")


class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def talk(self):
        return "Meow!"


class Dog(Animal):
    def talk(self):
        return "Woof Woof"


animals = [Cat("Missy"), Dog("mistoffeless"), Dog("lassie")]
for animal in animals:
    print(animal.name + " : " + animal.talk())


# NotImplementedError : 자식 클래스에만 해당 함수를 사용할 수 있도록 함


class Product(object):
    pass


class Inventory(object):
    def __init__(self):
        self.__items = []

    def add_new_item(self, product):
        if (type(product) == Product):
            self.__items.append(product)
            print("new item added")
        else:
            raise ValueError("Invalid Item")

    def get_number_of_items(self):
        return len(self.__items)

    @property
    def items(self):
        return self.__items


inven = Inventory()
inven.add_new_item(Product())
inven.add_new_item(Product())

items = inven.items
items.append(Product())

# 클래스 내부용으로만 변수를 사용하고 싶다면 '__변수명' 형태로 변수를 선언한다.
# 가시성을 클래스 내로 한정하면서 값이 다르게 들어가는 것을 막을 수 있다. : 정보은닉
# 클래스 외부에서 사용하기 위해서는 데코레이터라고 불리는 @property 사용
