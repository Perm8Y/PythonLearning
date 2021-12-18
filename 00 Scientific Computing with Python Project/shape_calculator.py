class Rectangle():
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    def __str__(self):
        return(f"Rectangle(width={self.width}, height={self.height})")
    
    def set_width(self, w):
        setattr(self, "width", w)
    
    def set_height(self, h):
        setattr(self, "height", h)
    
    def get_area(self):
        return (self.width*self.height)
    
    def get_perimeter(self):
        return (2*self.width + 2*self.height)

    def get_diagonal(self):
        return ((self.width**2 + self.height**2)**0.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            print("Too big for picture")
        else:
            line = "*" * int(self.width)
            for i in range(int(self.height)):
                print(line)

    def get_amount_inside(self, another_shape):
        if another_shape.width*another_shape.height > self.width*self.height:
            print("Input shape is bigger than this shape")
        else:
            print(another_shape.width*another_shape.height // self.width*self.height)


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(self, side)
        self.width = side
        self.height = side

    def __str__(self):
        super().__str__()
        return(f"Square(side={self.width})")

    def set_side(self, side):
        setattr(self, "width", side)
        setattr(self, "hieght", side)

    def set_width(self, w):
        super().set_width()
        setattr(self, "width", w)
        setattr(self, "hieght", w)
    
    def set_height(self, h):
        super().set_height()
        setattr(self, "width", h)
        setattr(self, "height", h)