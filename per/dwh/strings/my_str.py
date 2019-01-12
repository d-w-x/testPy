# =====================format============================

# ============================
strings = "{} is good day, {}"
print(strings.format("1.12", "hello"))

# ============================
strings = "{1} is good day, {0}"
print(strings.format("hello", "1.12"))

# ============================
strings = "{0[0]} is good day, {0[1]}"
args = ["1.12", "hello"]
print(strings.format(args))  # 3: 1.12 is good day, hello

# ============================
strings = "{}: {date} is good day, {greeting}"
print(strings.format(3, greeting="hello", date="1.12"))  # 3: 1.12 is good day, hello

# ============================
keys = {"greeting": "hello", "date": "1/12"}
print(strings.format(3, **keys))

# ============================
print('{:*^10}'.format('ABC12abc') + "1")

# ============================
print("{:d}".format(-0x1100))

# ============================
print('{:,}'.format(123456789))
print('{:d}'.format(0x123a))
print('{:4<8}'.format(0x123a))
print("{{0}}的转义.{}".format("111", "222"))
