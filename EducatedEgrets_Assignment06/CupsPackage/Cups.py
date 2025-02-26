# File Name : Cups.py
# Student Name: Omar Alkhawaga
# email: alkhawoe@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 2/27/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The assignment is to develop a VS project modeling something in the real world with peers.
# Brief Description of what this module does: This module provides class about Cups in the book store and returns something cool
# Citations: https://stackoverflow.com/questions/71078674/how-do-getters-and-setters-work-in-python (setter and getters)
# Anything else that's relevant: N/A


class Cup:
    def __init__(self, material, capacity, price):
        """
        @param material String: The material of cup
        @param price int: The price of the cup
        @param capacity int: The capacity of the cup 
        """
        self.material = material
        self.capacity = capacity
        self.price = price
        self.is_filled = False

    def __str__(self):
        """
        @return: A string containing the material, capacity, price of the cup
        """
        return f"Cup(material={self.material}, capacity={self.capacity}ml, price=${self.price})"

    def __repr__(self):
        return self.__str__()

    @property
    def material(self):
        """
        Get the material of the cup.
        @return: The material of the cup.
        """
        return self._material

    @material.setter
    def material(self, value):
        """
        @param value: The new material of the cup.
        """
        self._material = value

    def fill(self):
        """
        Fills the tumbler with a specified beverage.
        @param beverage: The beverage to fill the cup with.
        @return: A string indicating the cup has been filled.
        """
        self.is_filled = True
        return "The cup is now filled with a beverage."