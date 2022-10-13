from __future__ import annotations # for type hinting, |-operator
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from math import pi, dist

class Shape: # super class of gemetrical shapes
    """Super class of gemetrical shapes: Circle & Rectangle"""

    def __init__(self, x_position: (int|float) = 0, y_position: (int|float) = 0) -> None:
        """init method of Shape class, takes x,y coordinates of shape"""

        self.x_position = x_position
        self.y_position = y_position

    # String representation

    def __repr__(self) -> str:
        return f"Shape(x_position = {self.x_position}, y_position = {self.y_position})"

    def __str__(self) -> str:
        return f"Shape wth x: {self.x_position}, y: {self.y_position}"

    # Getter, setter for x_position

    @property
    def x_position(self) -> int | float:
        return self._x_position
    
    @x_position.setter
    def x_position(self, value: int | float) -> int | float:

        print("x_position")
        if not isinstance(value, (int,float)):
            raise TypeError(f"x_position must be a number, not {type(value)}")
        
        self._x_position = round(value, 1)



    # Getter, setter for y_position

    @property
    def y_position(self) -> int | float:
        return self._y_position

    @y_position.setter
    def y_position(self, value: int | float) -> int | float:
        if not isinstance(value, (int, float)):
            raise TypeError(f"y_position must be a number, not {type(value)}")
        
        self._y_position = round(value, 1)


    
    # Overloading

    # smaller than
    def __st__(self, other: Shape) -> bool:
        """Override of smaller than '<' operator"""
        if not type(self) == type(other):
            raise TypeError(f"Cannot compare {self} with {other}")
        return self.area < other.area

    # equal to
    def __eq__(self, other: Shape) -> bool:
        """Override of equal '==' operator"""
        if not type(self) == type(other):
            raise TypeError(f"Cannot compare {self} with {other}")
        return self.area == other.area

    # greater than
    def __gt__(self, other: Shape) -> bool:
        """Override of greater than '>' operator"""
        if not type(self) == type(other):
            raise TypeError(f"Cannot compare {self} with {other}")
        return self.area > other.area
    
    # smaller or equal
    def __se__(self, other: Shape) -> bool:
        """Override of smaller or equal, '<=' operator"""
        if not type(self) == type(other):
            raise TypeError(f"Cannot compare {self} with {other}")
        return self.area <= other.area

    # greater or equal
    def __ge__(self, other: Shape) -> bool:
        """Override of greater or equal, '>=' operator"""
        if not type(self) == type(other):
            raise TypeError(f"Cannot compare {self} with {other}")
        return self.area >= other.area

    
    # translate method

    def translate(self, x: (int | float) = 0, y: (int | float) = 0) -> None:
        """Moves shape x,y distance units"""
        self.x += x
        self.y += y

    # ======== KOM TILLBAKA TILL DENNA DELEN ======== #

    def plot_translation(self, x: (int | float) = 0, y: (int | float) = 0) -> None:
        """Translate the shapes and also plot them"""
        patch_list = [] # storing values in this list

        patch_list.append(self.plot())
        patch_list[0].set_alpha(0.3)

        self.translate(x,y)
        patch_list.append(self.plot())
        return patch_list

    
class Circle(Shape): # subclass to Shape(). Inherits from Shape()
    """subclass to Shape(), creates a circle that inherits from Shape()"""
    def __init__(self, x_position: int|float = 0, y_position: int|float = 0, radius: int|float = 1) -> None:
        super().__init__(x_position, y_position)
        self._radius = radius

    # property for values of Circle; radius, circumference and area.

    @property
    def radius(self) -> (int | float):
        """Radius of circle"""
        return self._radius
    
    @radius.setter
    def radius(self, value) -> (int | float):
        if isinstance(value, (float)): # for some reason i can't write (int | float) here.
            raise TypeError(f"The radius has to be an int or float, not {type(value)}")
        if value <= 0:
            raise ValueError(f"Radius must be larger than 0")
        self._radius = value

    
    @property
    def circumference(self) -> (int | float):
        """Circumference"""
        return 2*pi*self._radius # way to calculate circumference

    @property
    def area(self) -> (int | float):
        """Area of the circle"""
        return pi*self._radius**2 # way to calculate area of an circle


    # String conversion

    def __repr__(self) -> None:
        return f"Circle with x_pos = {self.x_position}, Circle with y_pos = {self.y_position}, radius is = {self.radius}"
    
    def __str__(self) -> None:
        return f"Circle with x_pos = {self.x_position} Circle with y_pos = {self.y_position}, radius is = {self.radius}, circumference is = {self.circumference}"
    
    # some more cool methods

    def __eq__(self, other: int | float): # checks if the area is the same -> returns true
        return self.area == other

    def is_unit_circle(self) -> bool:
        """Checks if the circle is a unit circle"""
        if self.radius == 1 and self.x_position == 0 and self.y_position == 0:
            return True
        return False

    # Thanks to Daniel and Stackoverflow.
    # https://stackoverflow.com/questions/481144/equation-for-testing-if-a-point-is-inside-a-circle
    def is_inside_circle(self, x, y) -> bool:
        """Calculation of euclidian distance of the new points compared to first x,y points. Has radius of circle too."""
        return (x - self.x_position)**2 + (y - self.y_position)**2 < self.radius**2

    

class Rectangle(Shape): # same as the subclass Circle. Inhertis from upperclass, Shape()
    """Rectangle class"""
    def __init__(self, x_position: float, y_position: float, base: float, height: float):
        super().__init__(x_position, y_position)
        self.base = base
        self.height = height

    """String conversion for Rectangle()"""
    def __repr__(self) -> str:
        return f"{self.x_position}{self.y_position}{self.base}{self.height}"

    def __str__(self) -> str:
        return f"Rectangles X-position is: {self.x_position}. Y-position is: {self.y_position}. Base: {self.base}. Height: {self.height}"


    @property
    def base(self) -> (int | float):
        return self._base

    @base.setter
    def base(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Number must be an int or float, not {type(value)}")
        if not (0 <= value <= 10):
            raise ValueError("Number must be between 0 and 10")
        self._base = value

    @property
    def height(self) -> (int | float):
        return self._height

    @height.setter
    def height(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Number must be an int or float, not {type(value)}")
        if not (0 <= value <= 10):
            raise ValueError("Number must be between 0 and 10")
        self._height = value

    @property # calculate circumference of Rectangle
    def circumference(self) -> int:
        """Circumference of Rectangle"""
        return (self.base + self.height)**2

    @property # calculate area of Rectangle
    def area(self) -> int:
        """Area of Rectangle"""
        return self.base * self.height

    # Methods for Rectangle



    def true_square(self) -> bool:
        """This method is checking if the base and height are of the same value. If they are it's a proper Rectangle."""
        if self.base == self.height:
            return True
        else:
            return False

    # got a lot of help from Andreas and Daniel for writing this method
    def is_inside_rectangle(self, x, y) -> bool:
        """Checks if point is inside rectangle"""
        if self.x_position - self.width / 2 <= x <= self.x_position + self.width / 2 and self.y_position - self.height / 2 <= y <= self.y_position + self.height / 2:
            return True
        return False
    
