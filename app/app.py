
from app.cone import Cone

if __name__ == "__main__":
  
    Cone.about()
    cone = Cone(5, 10)
 
    cone.dump()
from app.shape import Shape
import math

class Cone(Shape):
    def __init__(self, radius, height):
        super().__init__()  
        self.__radius = radius  
        self.__height = height 

    def volume(self):
        """Метод для расчета объема конуса."""
        return (1 / 3) * math.pi * (self.__radius ** 2) * self.__height

    def dump(self):
        """Метод для вывода объема конуса."""
        print(f"Объем конуса с радиусом {self.__radius} и высотой {self.__height} равен {self.volume()}")
