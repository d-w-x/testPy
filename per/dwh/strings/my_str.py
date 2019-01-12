# =====================format============================
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

# ============================
date = "1/12"
greeting = "hello"
print(f"{greeting.capitalize()},today is {date}")

# =====================other============================
print("============================")
a = u" 12a4sDf\t1d马 "
print(a.capitalize())
print(a.center(20) + "~")
print(a.count("1", 2, -4))
b = a.encode("GBK")
print(b)
print(b.decode("GBK", "replace"))
print(a.endswith(("1", "2", "3", "4")))
print(a.expandtabs())
print(a.index("4"))
print("============================")
print(a.isalpha())
print(a.islower())
print("2".islower())
print(a.isidentifier())
print("class".isidentifier())
print("============================")
print("-".join("32423"))
print(a.ljust(30) + "1")
print(a.lower())
print(a.lstrip())
print(str.maketrans("Dd", "][", "马"))
print(a.translate(str.maketrans("Dd", "][", "马")))
print(a.__len__())
print(max(a))
print(a.replace("1", "7"))
print(a.split(" "))
print(a.startswith(("1", "2")))
print(a.zfill(50))
