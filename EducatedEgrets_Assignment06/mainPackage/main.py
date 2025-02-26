# main.py

# File Name : EducatedEgrets_Assignment06
# Student Name: Abel Yemaneab
# email:  yemaneag@mail.uc.edu
# Assignment Number: Assignment 06  
# Due Date:   02/35/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment is to develop and simulate a real world object with peers

# Brief Description of what this module does: This module teaches us to use classes, getters, and setters in a python project
# Citations: https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/ 

# Anything else that's relevant:

from CupsPackage.Cups import *
from bookPackage.book import *
from ShirtsPackage.Shirts import *

if __name__ == "__main__":

    # This project simulates a bookstore and the objects you might find in it

    # Book Section

    # Instantiate a Book 
    book1 = Book("Fiction", 20, 10)
    book2 = Book("Non-Fiction", 25, 5)
    # Printing Initial Book Info
    print("Initial Book Details:")
    print(book1)
    print(book2)
    print("")

    # Getter
    print(f"Book1 is a {book1.get_type()} book costing ${book1.get_price()} and we have {book1.get_quantity()} in stock.") 
    print(f"Book2 is a {book2.get_type()} book costing ${book2.get_price()} and we have {book2.get_quantity()} in stock.") 
    print("")
    
    # Updating book properties using setters
    book1.set_price(28)
    book1.set_quantity(50)
    book2.set_price(18)
    book2.set_quantity(10)
    
    # Display update
    print("The updated book prices are:")
    print(book1)
    print(book2)
    print("")

    # Display book selling functionality
    book1.sell_books(4)
    print(book1)
    book2.sell_books(11) #This shows the exception handler for the sell_books function
    print(book2)
    print("")
    
    #Final Book Details
    print("Final Book Details:")
    print(book1)
    print(book2)
    print("")

    # Shirt Section
 
    # Instantiate a Shirt
    shirt1 = Shirt("Adidas", "L", "Blue", 35.99)

    #Printing Initial Shirt Info
    print("Initial Shirt Details")
    print(shirt1)
    print("")
    
    # get shirt info using getters
    print("Shirt Details Using Getters:")
    print(f"This shirt is a {shirt1.brand} shirt, being size {shirt1.size}, its color is {shirt1.color}, and it costs ${shirt1.price}")

    
    # Updating Shirt Properties using setters
    shirt1.price = 32.99
    shirt1.change_color("Green")
    print("")
    
    # Display Update
    print("Updated Shirt Details:")
    print(shirt1)
    print("")
    
    # Changing color
    print("Updated Shirt Color:")
    print(shirt1.change_color("White"))
    print("")
    
    # Print final details
    print("Final Shirt Details:")
    print(shirt1)
    print("")

    # Cup Section

    # Instantiate a Cup
    cup1 = Cup("Plastic", 200, 9.99)

    #Printing Initial Cup Info
    print("Initial Cup Details:")
    print(cup1)
    print("")

    # get cup info using getters
    print("Shirt Details Using Getters:")
    print(f"This cup is made of {cup1.material}, it can hold {cup1.capacity}ml, and it costs ${cup1.price}")
    print("")

    # updating cup properties with setters
    cup1.material = "Ceramic"
    cup1.capacity = 1000
    cup1.price = 99.99

    # updated cup properties
    print("Updated Cup Properties:")
    print(cup1)
    print("")

    # Filling Cup
    print("Filling Cup Up:")
    print(cup1.fill())
    print("")

    # Print final Cup Details
    print("Final Cup Details:")
    print(cup1)