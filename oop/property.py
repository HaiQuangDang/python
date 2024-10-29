class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def print_rectangle(self):
        print(f"This rectangle has width {self._width} cm and height {self._height} cm")

    @property
    def width(self):
        return f"{self._width} cm"

    @property
    def height(self):
        return f"{self._height} cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


    

    
rec1 = Rectangle(3, 4)
print(rec1._width)
print(rec1._height)

rec1.width = 0
rec1.height = -1
print(rec1.width)
print(rec1.height)

rec1._width = -3
rec1._height = -4
print(rec1.width)
print(rec1.height)

del rec1.width
del rec1.height

