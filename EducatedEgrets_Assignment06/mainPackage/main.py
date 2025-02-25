# main.py
# File Name : EducatedEgrets_Assignment06
# Student Name: Abel Yemaneab
# email:  yemaneag@mail.uc.edu
# Assignment Number: Assignment 06  
# Due Date:   02/35/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  {required}

# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
# Citations: {"Stack Overflow" is not sufficient. Provide repeatable links, book page #, etc.}

# Anything else that's relevant:

from bookPackage.book import *
from ShirtsPackage.Shirts import *

if __name__ == "__main__":
    # Instantiate a Book object
    book1 = Book("Fiction", 20, 10)
    book2 = Book("Non-Fiction", 25, 5)
    # Print Book Info
    print("Initial Book Details:")
    print(book1)
    print(book2)
    #Getter
    print(f"Book1 is a {book1.get_type()} book costing ${book1.get_price()} and we have {book1.get_quantity()} in stock.") 
    print(f"Book2 is a {book2.get_type()} book costing ${book2.get_price()} and we have {book2.get_quantity()} in stock.") 

    # Updating book properties
    book1.set_price(28)
    book1.set_quantity(50)
    book2.set_price(18)
    book2.set_quantity(10)
    # Display update
    print("The updated book prices are")
    print(book1)
    print(book2)
    # Display book selling functionality
    book1.sell_books(4)
    print(book1)
    book2.sell_books(11) #This shows the exception handler for the sell_books function
    print(book2)
    