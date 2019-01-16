class A:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)

    def __bool__(self):
        return False

    def __contains__(self, item):
        return self.name.__contains__(item)

    def __lt__(self, other):
        return self.name < other.name


print(bool(""))
a = A("erts")
print(bool(a))

print(bool(not 0 == 1))

print(a == "erts")

print("erts" == "erts")

b = A("erts")
print(a is b)

print("e" in a)

a = A(1)
b = A(2)
print(a < b)
# print(a > b)  #expection
