import re

number_one = 4500000
def to_string():
    print(f"{number_one:,}")
to_string()

number_two = 67
def to_decimal():
    print(f"{number_two:.2f}")
to_decimal()

number_three = 5600
def add_plus():
    print(f"{number_three:+}")
add_plus()

number_four = -430000
def add_comma():
    print(f"{number_four:,}")
add_comma()

number_five = 45.6789
def two_decimal():
    print(f"{number_five:.2f}")
two_decimal()

number_six = 9999.999
def round_up():
    print(f"{number_six:.2f}")
round_up()

number_seven = 10000
def add_k():
    print(f"{number_seven // 1000:}K")
add_k()

number_eight = 2500000
def add_m():
    print(f"{number_eight // 1000000:}M")
add_m()

# Regex
search = re.search(r"\d+","abc123xyz")
print(search.group())

find_all = re.findall(r"\d+","abc123xyz")
print(find_all)

the_caret = re.findall(r"^","abc123xyz")
print(the_caret)

the_dot = re.findall(r".","abc123xyz")
print(the_dot)

the_asterisk = re.findall(r".*","abc123xyz")
print(the_asterisk)
