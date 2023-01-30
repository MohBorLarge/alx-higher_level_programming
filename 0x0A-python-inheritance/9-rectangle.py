#!/usr/bin/python3
B = __import__('7-base_geometry').BaseGeometry
"""
===================================
module with class BaseGeometry
===================================
"""


class Rectangle(B):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(iself, width, height):
        """Method for initialized the attrubutes"""
        """

        This function makes Instantiation of width and height

        """

        self.integer_validator("width", width)

        self.integer_validator("height", height)

        self.__width = width

        self.__height = height

        def area(self):

            """

            This function computes the area of the rectangle.

            """

            return self.__height * self.__width

        def __str__(self):

            """

            The string representation of the instances of the class

            Rectangle with magic method __str__().

            """

            return ("[" + str(self.__class__.__name__) + "] " +

                    str(self.__width) + "/" + str(self.__height))
