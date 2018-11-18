# def table1():
#     amount = 1500
#     number_of_people = 3
#     print(f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円")
#
#
# def table2():
#     amount = 2000
#     number_of_people = 3
#     print(f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円")
#
#
# def table3():
#     amount = 3647
#     number_of_people = 4
#     print(f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円")
#
#
# table1()
# table2()
# table3()


def warikan(amount, number_of_people):
    return f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円"


result1 = warikan(1500, 3)
result2 = warikan(2000, 3)
result3 = warikan(3647, 4)
print(result1)
print(result2)
print(result3)
