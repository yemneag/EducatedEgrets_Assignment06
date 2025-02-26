#Shirts.py

# File Name : EducatedEgrets_Assignment06
# Student Name: Rithu Aynampudi
# email: aynampru@mail.uc.edu
# Assignment Number: Assignment06
# Due Date: 02/27/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This assignment is a group project which models the UC Bookstore
# Brief Description of what this module does: This module shows us how to create classes and provide properties related to a topic in the real world
# Citations: W3Schools (https://www.w3schools.com/python/default.asp), realpython(https://realpython.com/)



class Shirt:
    def __init__(self, brand: str = "Nike", size: str = "M", color: str = "Red", price: float = 29.99):
        """
        Constructor for Shirt class
        @param brand String: The brand of the shirt
        @param size String: The size of the shirt
        @param color String: The color of the shirt
        @param price float: The price of the shirt
        """
        self._brand = brand;
        self._size = size
        self._color = color
        self._price = price

    def __str__(self):
        """
        @return String: A formatted string representation of the shirt details
        """
        return f"Shirt Details - Brand: {self._brand}, Size: {self._size}, Color: {self._color}, Price: ${self._price:.2f}"

    def __repr__(self):
        """
        @return String: A string representation of the shirt object in code format
        """
        return f"Shirt('{self._brand}', '{self._size}', '{self._color}', {self._price})"

    @property
    def brand(self):
        """
        @return String: The brand of the shirt
        """
        return self._brand

    @property
    def size(self):
        """
        @return String: The size of the shirt
        """
        return self._size

    @property
    def color(self):
        """
        @return String: The color of the shirt
        """
        return self._color

    @color.setter
    def color(self, new_color: str):
        """
        Set a new color for the shirt
        @param new_color String: The new color to be set for the shirt
        """
        self._color = new_color

    @property
    def price(self):
        """
        @return float: The price of the shirt
        """
        return self._price

    @price.setter
    def price(self, new_price: float):
        """
        Set a new price for the shirt, ensuring it's greater than 0
        @param new_price float: The new price to be set for the shirt
        """
        if new_price > 0:
            self._price = new_price
        else:
            raise ValueError("Price must be greater than zero.")

    def change_color(self, new_color: str):
        """
        Change the color of the shirt
        @param new_color String: The new color for the shirt
        @return String: A confirmation message of the color change
        """
        self.color = new_color
        return f"The shirt color has been changed to {self._color}."




