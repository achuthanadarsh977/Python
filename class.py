

# class MyPoly:
#     x = 5


# poly = MyPoly()
# print(poly.x)

# print(type(poly))

# class Poly1:

#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def first(self):
#         print(f'First number:{self.x}')
    
#     def second(self):
#         print(f'Second number:{self.y}')


# p = Poly1(23,34)
# p.first()
# p.second()

class Poly2:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self):
        print(f'Sum of two numbers:{self.x+self.y}')

p = Poly2(12,23)
p.sum()
        