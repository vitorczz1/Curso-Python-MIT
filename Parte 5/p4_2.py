import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def euclidean_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz)

class Triangle:

    def __init__(self, x, y, z):
        self.x = x # = A
        self.y = y # = B
        self.z = z # = C
    
    def side_lengths(self):
        point = Point(self.y.x, self.y.y)
        point2 = Point(self.z.x, self.z.y)
        point3 = Point(self.x.x, self.x.y)

        p = (point.euclidean_distance(self.x), point2.euclidean_distance(self.y), point3.euclidean_distance(self.z))
        return p
    
    def angles(self):
      inst = Triangle(self.x, self.y, self.z)
    
      #AB
      angulo_AB = Point(self.y.x, self.y.y)
      angulo_AB1 = angulo_AB.angle_between(self.x)

      #BA
      angulo_BA = Point(self.x.x, self.x.y)
      angulo_BA1 = angulo_BA.angle_between(self.y)

      #BC
      angulo_BC = Point(self.z.x, self.z.y)
      angulo_BC1 = angulo_BC.angle_between(self.y)

      #CB
      angulo_CB = Point(self.y.x, self.y.y)
      angulo_CB1 = angulo_CB.angle_between(self.z)

      #AC
      angulo_AC = Point(self.z.x, self.z.y)
      angulo_AC1 = angulo_AC.angle_between(self.x)

      #CA
      angulo_CA = Point(self.x.x, self.x.y)
      angulo_CA1 = angulo_CA.angle_between(self.z)

      angulo_01 = (angulo_CA1 - angulo_BA1)
      angulo_02 = (angulo_AB1 - angulo_CB1)
      angulo_03 = (angulo_CB1 - angulo_CA1)

      angulo_01 *= 180/math.pi
      angulo_02 *= 180/math.pi
      angulo_03 *= 180/math.pi

      radiano1 = math.radians(angulo_01)
      radiano2 = math.radians(angulo_02)
      radiano3 = math.radians(angulo_03)

      return (radiano1, radiano2, radiano3)

    def side_classification(self):
        inst = Triangle(self.x, self.y, self.z)

        x = inst.side_lengths()

        if (math.isclose(x[0], x[1]) and math.isclose(x[2], x[0]) and math.isclose(x[1], x[2])):
            return ("equilateral")

        elif ((x[0] == x[1]) or (x[1] == x[2]) or (x[2] == x[0])):
            return ("isosceles")
        
        elif ((x[0] != x[1]) and (x[2] != x[0])):
            return ("scalene")

    def angle_classification(self):
        inst = Triangle(self.x, self.y, self.z)

        x = inst.angles()

        if (math.isclose(x[0], x[1]) and math.isclose(x[2], x[0])): #60 graus radianos
            return ("equiangular")

        elif ((x[0] < 1.5707963267948966) and (x[1] < 1.5707963267948966) and (x[2] < 1.5707963267948966)): #90 graus radianos
            return ("acute")
        
        elif((x[0]  == 1.5707963267948966) or (x[1]  == 1.5707963267948966) or (x[2] == 1.5707963267948966)): #90 graus radianos
            return ("right")
        
        elif((x[0] > 1.5707963267948966) or (x[1] > 1.5707963267948966) or (x[2] > 1.5707963267948966)): #90 graus radianos
            return ("obtuse")
        
    def is_right(self):
        inst = Triangle(self.x, self.y, self.z)

        x = inst.side_lengths()

        print(x)

        c1 = x[0]
        c2 = x[1]
        c3 = x[2]

        c1final = (c1 ** 2)
        c2final = (c2 ** 2)
        c3final = (c3 ** 2)

        final = c1final + c3final

        final2 = c2final - final

        if (final2 == 0 and final2 <= (10 ** -6)):
            return True
        else:
            return False

    def area(self):
        inst = Triangle(self.x, self.y, self.z)

        x = inst.side_lengths()

        d = (((self.x.x * self.y.y) + (self.x.y * self.z.x) + (self.y.x * self.z.y)) - ((self.x.y * self.y.x) + (self.x.x * self.z.y) + (self.y.y * self.z.x)))
    
        area = d / 2
        return area

    def perimeter(self):
        inst = Triangle(self.x, self.y, self.z)

        x = inst.side_lengths()
        
        total = 0

        for i in x:
            total += i
        return total