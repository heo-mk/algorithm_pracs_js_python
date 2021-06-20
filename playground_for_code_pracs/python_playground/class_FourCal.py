class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4,2)
# a.add()
# a.setdata(4, 2)
print(a.first)
print(a.second)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print()

# b = FourCal()
# b.setdata(3, 7)
# print(b.first)
# print(a.first)
# print(b.add())
# print(b.mul())
# print(b.sub())
# print(b.div())
# print()

# c = FourCal()
# d = FourCal()
# c.setdata(4, 2)
# d.setdata(3, 7)
# print(id(c.first))
# print(id(d.first))
print()

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

e = MoreFourCal(10, 20)
print(e.add())
print(e.mul())
print(e.sub())
print(e.div())
print(e.pow())
print()

# f = FourCal(4, 0)
# print(f.div())

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

g = SafeFourCal(4, 0)
print(g.div())  
print()

# 클래스 변수
class Family:
    lastname = "김"

print(Family.lastname)

h = Family()
i = Family()
print(h.lastname)
print(i.lastname)
print()

Family.lastname = "박"
print(h.lastname)
print(i.lastname)

print(id(Family.lastname))
print(id(h.lastname))
print(id(i.lastname))

