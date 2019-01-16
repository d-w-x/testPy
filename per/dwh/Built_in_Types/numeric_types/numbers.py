import sys
from math import trunc

print(sys.float_info)

a = 1027
b = 17
c = 7.0019
d = 4 + 1J
e = "23"
f = "23.432"
g = "3+4J"
# =========================================
print(a / b)
print(a % b)
print(divmod(a, b))
print(a / c)
print(a // c)
print(a % c)
print(int(e) + a)
print(float(f) + c)
print(complex(a, b) + complex(g))
print(trunc(-9.9999))
print(round(4.11111111, 3))

# ========================
print(-2 >> 1)

print(bin(a))
print(a.bit_length())
print(bin(-a))
print((-a).bit_length())
print(a.to_bytes(2, "big"))
print((-a).to_bytes(2, "big", signed=True))
print(int.from_bytes(b'\xfb\xfd', "big"))
print(int.from_bytes(b'\xfb\xfd', "big", signed=True))

# ========================
print(c.as_integer_ratio())
print(1234.0.is_integer())
print(c.is_integer())
print(0.5.hex())
print(float.fromhex('0x1.0000000000000p-1'))

print(a.__hash__())
print(1027.0.__hash__())
print(c.__hash__())

print(sys.hash_info)
