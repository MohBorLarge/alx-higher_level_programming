#!/usr/bin/python3

"""
===================================
module with class Rectangle
===================================
"""
B = __import__('7-base_geometry').BaseGeometry


class Rectangle(B):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """using integer validator """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
