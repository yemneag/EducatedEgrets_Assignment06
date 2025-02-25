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

if __name__ == "__main__":
    # Instantiate a Book object
    book1 = Book("Fiction", 20, 10)
    book2 = Book("Non-Fiction", 25, 5)
    # Print Book Info
    print("Initial Book Details:")
    print(book1)
    print(book2)
    #Getter
    print(f"Book1 is a {book1.get_type()} book with the price of {book1.get_price()} and we have {book1.get_quantity()} in stock.") 