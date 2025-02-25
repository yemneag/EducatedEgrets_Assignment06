# books.py

# File Name : books.py
# Student Name: Kengo Ishizuka
# email: ishizuko@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 2/27/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The assignment is to develop a VS project modeling something in the real world with peers.

# Brief Description of what this module does: This module provides class about books.
# Citations: https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/

# Anything else that's relevant:

class Book:
    def __init__(self,type, price, quantity):
        """
        Constructor for Book class
        @param type String: The type of books
        @param price int: The price of the book
        @param quantity int: The quantity of the book
        """
        if type is None or not isinstance(type, str) or type.strip() == "":
            raise ValueError("Type cannot be blank, empty, or None.")
        if price < 0:
            raise ValueError("Price of a book cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity of a book cannot be negative")

        self.__type = type
        self.__price = price
        self.__quantity = quantity

    def set_type(self, type):
        """
        Assign a value to the book type of the current object
        @param type String: The book type to be assigned.
        """
        self.__type = type
    def get_type(self):
        """
        @return String: The book type of the current object
        """
        return self.__type

    def set_price(self, price):
        """
        Assign a value to the price of the book of the current object
        @param price int: The price of the book to be assigned.
        """
        self.__price = price
    def get_price(self):
        """
        @return int: The price of the book of the current object
        """
        return self.__price

    def set_quantity(self, quantity):
        """
        Assign a value to the quantity of the book of the current object
        @param quantity int: The quantity of the book to be assigned.
        """
        self.__quantity = quantity
    def get_quantity(self):
        """
        @return int: The quantity of the book of the current object
        """
        return self.__quantity

    def sell_books(self, amount):
        """
        Calculate the quantity of the book remaining of the current object
        @param int: The quantity of the book sold
        @return string: The quantity of books remaining of the current object or message if the quantity is not enough 
        """
        if amount > self.__quantity:
            print("Not enough stock to sell that many books!")
        else:
            self.__quantity -= amount
            print(f"Sold {amount} books. Remaining stock: {self.__quantity}")



    def __str__(self):
        """
        @return String: A formatted string representation of the book details
        """
        return "Book Type:" + str(self.__type) + ", " +"Price:" + str(self.__price) + ", " + "Quantity:" + str(self.__quantity)



