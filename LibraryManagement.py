from abc import ABC, abstractclassmethod

class Book(ABC):
    def __init__(self, Name,ID, Category, Status, author):
        self.Name=Name
        self.__ID=ID #private
        self.Category=Category
        self.__Status = Status #private
        self.author=author
    
    def get_Status(self):
        return self.__Status
    
    def set_Status(self, Status):
        if Status == 'borrowed':
            print( self.__Status)
        
        elif Status == 'added':
            print( self.__Status)
        elif Status == 'retuned':
            print( self.__Status)
        
        else :
            print("Not Found")
    
    def get_info(self):
        return f"Name:{self.Name}, Category:{self.Category}, Status:{self.get_Status()}, author:{self.author}"
    
    @abstractclassmethod
    def Sale(self):
        pass
        


class FictionBook(Book):
        def __init__(self, Name, ID, Category, Status, author, Most_requested ):
            super().__init__(Name, ID, Category, Status, author )
            self.Most_requested=Most_requested
        def get_info(self):
           return f"Name:{self.Name}, Category:{self.Category}, Status:{self.get_Status()}, author:{self.author} , Most_requested:{self.Most_requested}"
       
        def Sale(self):
           print("Sale 10%")

class NonFictionBook(Book):
    def __init__(self, Name, ID, Category, Status, author, Most_requested):
        super().__init__(Name, ID, Category, Status, author)
        self.Most_requested= Most_requested  
          
    def get_info(self):
         return f"Name:{self.Name}, Category:{self.Category}, Status:{self.get_Status()}, author:{self.author} , Most_requested:{self.Most_requested}"  
    
    
    def Sale(self):
        print("Sale 20%")

class Gamesbook(Book):
    def __init__(self, Name, ID, Category, Status, author, type_of_game):
        super().__init__(Name, ID, Category, Status, author)
        self.type_of_game = type_of_game
        
        
    def get_info(self):
         return f"Name:{self.Name}, Category:{self.Category}, Status:{self.get_Status()}, author:{self.author} , type_of_game:{self.type_of_game}"
    
    
    def Sale(self):
        print("Sale 15%") 


class ScienceBook(Book):
    def __init__(self, Name, ID, Category, Status, author, edition):
        super().__init__(Name, ID, Category, Status, author)
        self.edition=edition
    
    def get_info(self):
         return f"Name:{self.Name}, Category:{self.Category}, Status:{self.get_Status()}, author:{self.author} , edition:{self.edition}"
    
    def Sale(self):
        print("NO SALE") 
        
        
        
FictionBook1 =FictionBook("The Fault in Our Stars", 1 , "Fiction", "Borrowed", "john Green","yes")
NonFictionBook1 = FictionBook("The 7 Habits of Highly Effective People", 2 , "NonFiction", "returned", "Stephen R. Covey", "No")
Gamesbook1=Gamesbook("Play Nice", 3 , "Games", "added", " Jason Schreier", "Entertainment")
ScienceBook1 = ScienceBook("The Laws of Medicine", 4 , "Science", "added", "Siddhartha Mukherjee", "11th") 



print(FictionBook1.Name)


#######library#############3


class LibraryManagementSystem:
    def __init__(self):
        self.books = []  

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def search_by_name(self, name):
        """Search for books by name."""
        results = [book for book in self.books if book.Name.lower() == name.lower()]
        return results

    def search_by_category(self, category):
        """Search for books by category."""
        results = [book for book in self.books if book.Category.lower() == category.lower()]
        return results

    def search_by_author(self, author):
        """Search for books by author."""
        results = [book for book in self.books if book.author.lower() == author.lower()]
        return results

    def display_books(self):
        """Display all books in the library."""
        if not self.books:
            print("The library is currently empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book.get_info())


library = LibraryManagementSystem()

library.add_book(FictionBook1)
library.add_book(NonFictionBook1)
library.add_book(Gamesbook1)
library.add_book(ScienceBook1)

print("\n--- All Books in the Library ---")
library.display_books()

# Search by name
print("\n--- Search by Name: 'The Fault in Our Stars' ---")
results = library.search_by_name("The Fault in Our Stars")
for book in results:
    print(book.get_info())

# Search by category
print("\n--- Search by Category: 'Science' ---")
results = library.search_by_category("Science")
for book in results:
    print(book.get_info())

# Search by author
print("\n--- Search by Author: 'Jason Schreier' ---")
results = library.search_by_author("Jason Schreier")
for book in results:
    print(book.get_info())
