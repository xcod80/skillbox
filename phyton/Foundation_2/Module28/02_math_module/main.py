import math
class MyMath:
    @classmethod
    def circle_len(cls, radius:float = 1):
        return 2 * math.pi * radius
    @classmethod
    def circle_sq(cls, radius:float =1):
        return math.pi * radius ** 2
    @classmethod
    def cube_vol(cls, len:float = 1):
        return len ** 3
    @classmethod
    def sphere_area(cls, radius:float =1):
        return 4 * math.pi * radius ** 2

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
