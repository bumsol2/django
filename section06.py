# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):

# 예제1

def hello(world):
    print("Hello", world)


hello("Python")
hello(7777)

# 예제


# def hello_return(world):
#     val = "Hello" + str(world)
#     return val


# str = hello_return("Python!!!!!")
# print(str)

# 예제3(다중리턴)


# def func_mul2(x):
#     y1 = x * 100
#     y2 = x * 200
#     y3 = x * 300
#     return [y1, y2, y3]


# It = func_mul2(100)
# print(It, type(It))

# 예제4
# *args, *kargs

def args_func(*args):
    # for t in args:
    #     print(t)
    for i, v in enumerate(range(10)):
        print(i, v)


args_func('kim')
args_func('kim', 'Park')
args_func('kim', 'Park', 'Lee')

# kwargs


# def kwargs_func(**kwargs):
#     for k, v in kwargs.items():
#         print(k, v)


# kwargs_func(name1='Kim', name2="Park", name3='Lee')

# 전체 혼합


def example_mul(arg1, arg2, *args, **kwargs):
        print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim', age1=24, age2=35)

# 중첩함수(클로저)
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)
