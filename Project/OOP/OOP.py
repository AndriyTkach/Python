import random
import time
from math import ceil,pi 
import RoomWallpaper
# 2 --------------------------------------------------------------

class Warrior:
    def setHealth(self, h):
        self.Health = h

    def setName(self, name):
        self.Name = name
    
    def attack(self, other):
        print("\nАтакует",self.Name,":")
        other.Health -= 20

def Task2():
    unit1 = Warrior()
    unit2 = Warrior()
    unit1.Name = "Unit 1"
    unit2.Name = "Unit 2"
    unit1.Health = 100
    unit2.Health = 100

    print(unit1.Name, "  ", unit2.Name)
    print(unit1.Health, "     ", unit2.Health)

    while True:
        if random.randrange(1,3,1) == 1:
            unit1.attack(unit2)
        else:
            unit2.attack(unit1)
        print(unit1.Name, "  ", unit2.Name)
        print(unit1.Health, "     ", unit2.Health)
        time.sleep(0.5)
        if unit1.Health==0:
            print("\nПобедитель",unit2.Name)
            break
        elif unit2.Health==0:
            print("\nПобедитель",unit1.Name)
            break
# ----------------------------------------------------------------
# 3

class Person:
    def __init__(self,name,surname,qual=1):
        self.Name = name
        self.Surname = surname
        self.Qualification = qual

    def printInfo(self):
        print("\nИмя:",self.Name)
        print("Фамилия:",self.Surname)
        print("Квалификация специалиста:",self.Qualification)

    def __del__(self):
        print("\nДо свидания, мистер",self.Name,self.Surname)


def Task3():
    P1 = Person("Andrii","Tkach",3)
    P2 = Person("Tonny","Iommi")
    P3 = Person("Van","Halen",2)

    min_qual = min(P1.Qualification,P2.Qualification,P3.Qualification)

    people = [P1,P2,P3]

    for i in people:
        i.printInfo()
    
    for i in people:
        if i.Qualification == min_qual:
            i.__del__()

    input()

# ----------------------------------------------------------------
# 4
class Unit:
    def __init__(self,num,team):
            self.Number = num
            self.Team = team

class Hero(Unit):
    Level = 1
    def NewLevel(self):
        self.Level +=1
        
class Soldier(Unit):
    def FollowHero(self,Hero):
        print("\nСолдат \"{s}\" следует за героем \"{h}\".".format(s=self.Number,h=Hero.Number))

def Task4():
    H1 = Hero(1,1)
    H2 = Hero(2,2)

    solN = int(input("Введите количество солдат: "))

    soldiers1 = []
    soldiers2 = []
    
    for i in range(solN):
        if random.randrange(1,3,1) == 1:
            soldiers1.append(Soldier(i,1))
        else:
            soldiers2.append(Soldier(i,2))

    print("\nКоличество солдат в команде 1:",len(soldiers1))
    print("Количество солдат в команде 2:",len(soldiers2))

    if max(len(soldiers1),len(soldiers2))==len(soldiers1):
        H1.NewLevel()
    elif max(len(soldiers1),len(soldiers2))==len(soldiers2):
        H2.NewLevel()

    soldiers1[random.randrange(0,len(soldiers1),1)].FollowHero(H1)

# ----------------------------------------------------------------
# 5

class A():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return str("({x},{y})".format(x=self.x,y=self.y))

    def __add__(self,other):
        return A(self.x + other.x, self.y + other.y)

    def __radd__(self,other):
        return A(self.x + other.x, self.y + other.y)

class B():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def Task5():
    a = A(2,5)
    b = B(2,1)

    c = b + a

    print(c)

# ----------------------------------------------------------------
# 6

class Table:
    def __init__(self,a,b,h):
        self.__a = a
        self.__b = b
        self.__h = h
    
    def setDimensions(self,length,width,height):
        self.__dict__['_Table__a'] = length
        self.__dict__['_Table__b'] = width
        self.__dict__['_Table__h'] = height

    def getLength(self):
        return self.__dict__['_Table__a']

    def getWidth(self):
        return self.__dict__['_Table__b']

    def getHeight(self):
        return self.__dict__['_Table__h']


def Task6():

    T1 = Table(5,5,3)
    
    print(T1.__dict__)

    T1.setDimensions(6,6,2)

    print("Длина стола:",T1.getLength())
    print("Ширина стола:",T1.getWidth())
    print("Высота стола:",T1.getHeight())

# ----------------------------------------------------------------
# 7
class WinDoor:
    def __init__(self, x, y):
        self.square = x * y

class Room:
    def __init__(self, x, y, z):      
        self.length = x
        self.width = y
        self.height = z
        self.wd = []
    def addWD(self, w, h):
        self.wd.append(WinDoor(w, h))
    
    def getSurface(self):
        return 2 * self.height * (self.length + self.width)

    def workSurface(self):
        new_square = self.getSurface()
        for i in self.wd:
            new_square -= i.square
        return new_square

    def getRolls(self,length,width):
        return self.workSurface() / (length*width)  

def Task7():

    R1 = Room(float(input("Введите длину комнаты: ")),
              float(input("Введите ширину комнаты: ")),
              float(input("Введите высоту комнаты: ")))
    
    d = int(input("Введите количество дверей: "))
    for i in range(0,d,1):
        R1.addWD(float(input("Введите высоту двери №{a}: ".format(a=i+1))),
                 float(input("Введите ширину двери №{a}: ".format(a=i+1))))
    
    w = int(input("Введите количество окон: "))
    for i in range(0,w,1):
        R1.addWD(float(input("Введите длину окна №{a}: ".format(a=i+1))),
                 float(input("Введите высоту окна №{a}: ".format(a=i+1))))
    
    print("Площадь оклеимаевой поверхности:",R1.workSurface())
    rolls = R1.getRolls(float(input("Введите длину одного рулона обоев: ")),
                        float(input("Введите ширину одного рулона обоев: ")))
    print("Необходимое количество рулонов:",rolls)
    
# ----------------------------------------------------------------
# 8
class Snow:
    def __init__(self,n):
        self.snowF = n

    def __call__(self,n):
        self.snowF = n

    def makeSnow(self,col):
        snowStr = ""
        row = ceil(self.snowF / col)
        k = 1
        for i in range(row):
            snowStr += '\n'
            for j in range(col):
                if k<=self.snowF:
                    snowStr += '*'
                    k+=1
                else:  
                    break
        return snowStr

    def __add__(self,n):
        self.snowF += n

    def __sub__(self,n):
        self.snowF -= n

    def __mul__(self,n):
        self.snowF *= n

    def __truediv__(self,n):
        self.snowF = round(self.snowF / n)


def Task8():
    S = Snow(12)
    print(S.makeSnow(4))
    S + 2
    print(S.makeSnow(3))
    S - 5
    Snow(9)
    print(S.makeSnow(2))
    S * 10
    print(S.makeSnow(9))
    S / 4
    print(S.makeSnow(6))

# ----------------------------------------------------------------
# 9
def Task9():

    R1 = RoomWallpaper.RoomM(float(input("Введите длину комнаты: ")),
                             float(input("Введите ширину комнаты: ")),
                             float(input("Введите высоту комнаты: ")))
    
    d = int(input("Введите количество дверей: "))
    for i in range(0,d,1):
        R1.addWD(float(input("Введите высоту двери №{a}: ".format(a=i+1))),
                 float(input("Введите ширину двери №{a}: ".format(a=i+1))))
    
    w = int(input("Введите количество окон: "))
    for i in range(0,w,1):
        R1.addWD(float(input("Введите длину окна №{a}: ".format(a=i+1))),
                 float(input("Введите высоту окна №{a}: ".format(a=i+1))))
    
    print("Площадь оклеимаевой поверхности:",R1.workSurface())
    rolls = R1.getRolls(float(input("Введите длину одного рулона обоев: ")),
                        float(input("Введите ширину одного рулона обоев: ")))
    print("Необходимое количество рулонов:",rolls)

# ----------------------------------------------------------------
# 10
def Task10():
    print(RoomWallpaper.__name__)
    print(RoomWallpaper.__doc__)
    print(RoomWallpaper.RoomM.__name__)
    print(RoomWallpaper.RoomM.__doc__)
    print(RoomWallpaper.RoomM.getRolls.__name__)
    print(RoomWallpaper.RoomM.getRolls.__doc__)

# ----------------------------------------------------------------
# 11
class Data:
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]

class Teacher:
    def __init__(self):
        self.work = 0
    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
            self.work += 1

class Pupil:
    def __init__(self):
        self.knowledge = []
    def take(self, info):
        self.knowledge.append(info)
    def forget(self):
        self.knowledge.pop(random.randrange(0,len(self.knowledge),1))

def Task11():
    lesson = Data('class', 'object', 'inheritance', 'polymorphism',
                  'encapsulation')
    marIvanna = Teacher()
    vasy = Pupil()
    pety = Pupil()
    marIvanna.teach(lesson[2], vasy, pety)
    marIvanna.teach(lesson[0], pety)
    print(vasy.knowledge)
    print(pety.knowledge)
    vasy.take(lesson[0])
    print(vasy.knowledge)
    vasy.forget()
    print(vasy.knowledge)

# ----------------------------------------------------------------
# 13
class Cylinder:
    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle*2 + side, 2)
    
    def __init__(self, diameter, high):
        self.dia = diameter
        self.high = high
        self.area = self.make_area(self.dia,self.high)
    
    def __setattr__(self, name, value):
        if name == 'dia' or name == 'high':
            self.__dict__[name] = value
            self.area = self.make_area(self.dia,self.high)
        elif name == 'area':
            print('Нелья присваивать значение площади поверхности')
    
    def __getattr__(self,name):
        if name == 'dia' or name == 'high' or name == 'area': 
            return self.__dict__[name]
  
def Task13():
    a = Cylinder(1,2)
    print(a.area)
    print(a.make_area(2, 2))
    a.dia = 3
    print(a.area)
    a.area = 5

# ----------------------------------------------------------------
# 14
class Random:
    def __init__(self,n,d1,d2):
        self.n = n
        self.d1 = d1
        self.d2 = d2
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.n > 0:
            self.n-=1
            return random.randrange(self.d1,self.d2)
        else:
            raise StopIteration

def Task14():
    R1 = Random(5,1,3)
    for i in R1:
        print(i)

    print('')
    R2 = Random(10,1,11)
    for i in R2:
        print(i)

# ----------------------------------------------------------------
# 15
def RandomF(n,d1,d2):
    for i in range(n):
        yield random.randrange(d1,d2)

def Task15():
    R1 = RandomF(5,1,4)
    
    for i in R1:
        print(i)

# ----------------------------------------------------------------

Task15()
