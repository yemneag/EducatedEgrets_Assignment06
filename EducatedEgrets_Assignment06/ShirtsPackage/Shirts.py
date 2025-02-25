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
        self._brand = brand
        self._size = size
        self._color = color
        self._price = price
    
    def __str__(self):
        return f"Shirt Details - Brand: {self._brand}, Size: {self._size}, Color: {self._color}, Price: ${self._price:.2f}"
    
    def __repr__(self):
        return f"Shirt('{self._brand}', '{self._size}', '{self._color}', {self._price})"
    
    @property
    def brand(self):
        return self._brand
    
    @property
    def size(self):
        return self._size
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, new_color: str):
        self._color = new_color
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price: float):
        if new_price > 0:
            self._price = new_price
        else:
            raise ValueError("Price must be greater than zero.")
    
    def change_color(self, new_color: str):
        self.color = new_color
        return f"The shirt color has been changed to {self._color}."



