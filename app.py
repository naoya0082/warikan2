def hello():
    print("Hello World")


hello()


def say_hello(name):
    print("Hi " + name)


say_hello("Bob")
say_hello("Naoya")


def double(number):
    return 2 * number


double(3)
result = double(3)
print(result)


# 1分課題
def str_combine(str1, str2):
    return str1 + str2


result = str_combine("kazma", "takahashi")  # kazma takahashi を返す
print(result)
