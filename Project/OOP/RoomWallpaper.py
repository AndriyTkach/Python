'''Модуль содержит класс комнаты и класс для добавления объектов, 
которые не входят в оклеиваемую площадь'''
   
class WinDoorM:
    '''Клас объекта, который нужно вычесть из оклеиваемой площади.
Конструктор принимает длину и ширину объкта и сохраняет его площадь'''
    def __init__(self, x, y):
        self.square = x * y

class RoomM:
    '''Клас комнаты, которою нужно обклеить.
Конструктор принимает длину, ширину и высоту комнаты'''
    def __init__(self, x, y, z):      
        self.length = x
        self.width = y
        self.height = z
        self.wd = []
    def addWD(self, w, h):
        '''Метод для добавления объктов, которые не входят в оклеиваемую площадь. 
Метод принимает длину и ширину объекта'''
        self.wd.append(WinDoorM(w, h))
    
    def getSurface(self):
        '''Метод для вычисления оклеиваемой площади без учёта других объектов'''
        return 2 * self.height * (self.length + self.width)

    def workSurface(self):
        '''Метод для вычисления оклеиваемой площади с учётом объектов, которые нужно вычесть'''
        new_square = self.getSurface()
        for i in self.wd:
            new_square -= i.square
        return new_square

    def getRolls(self,length,width):
        '''Метод возвращает необходимое количество рулонов обоев для оклеивания комнаты. 
Метод принимает длину и ширину одного рулона'''
        return self.workSurface() / (length*width) 
