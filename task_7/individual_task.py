import random


# ------------------------- Utility methods -------------------------
def print_divider(): print("--------------------------------------------------------")


# ------------------------- Task methods -------------------------
def define_type(value: object):
    print(f'{value} - {type(value)}')


def add_to_string(string: str, value: object) -> str:
    return string + f'_{value}'


# ------------------------- Start program -------------------------
# task 1
a_list = [123, 17.4, False, 55, "abc", 2.9, True, "xyz"]
print(a_list)
print_divider()

# task 2
for item in a_list:
    define_type(item)
print_divider()

# task 3
print("1) s[i] = x | a_list[2] = 999.9")
a_list[2] = 999.9
print(a_list)

print("2) s[i:j] = t | a_list[5:6] = [77, \"qwerty\", False]")
a_list[5:6] = [77, "qwerty", False]
print(a_list)

print("7) s.remove(x) | a_list.remove(False)")
a_list.remove(False)
print(a_list)
print_divider()

# task 4
s = "12345"
print(s)
s_divided = "_".join(s)
print(s_divided)
print_divider()

# task 5
b_list = list(s)
print(b_list)
print_divider()

# task 6
print(f'Min = {min(b_list)}')
print(f'Max = {max(b_list)}')



input('\nНажмите <ENTER> для завершения')

