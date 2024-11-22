class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "available"
        
class Member:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []
        
class Shelf:
    def __init__(self, id):
        self.id = id
        self.books_held = []
        
    def add_book(self, book):
        self.books_held.append(book)
        print(f"Successfully added {book.title} by {book.author} to shelf {self.id} in the library")

    def remove_book(self, book):
        if book in self.books_held:
            self.books_held.remove(book)
            print(f"Successfully removed {book.title} by {book.author} from shelf {self.id} in the library")
        else:
            print(f"Error: {book.title} by {book.author} is not on this shelf")
        
    def display_books(self):
        for book in self.books_held:
            print(f"{book.title} by {book.author} on shelf {self.id} is {book.status}")

class Library:
    def __init__(self):
        self.members = []
        self.shelves = []
        
    def add_shelf(self, shelf):
        if shelf not in self.shelves:
            self.shelves.append(shelf)
            print(f"Successfully added shelf {shelf.id} to the library")
        else:
            print(f"Error: Shelf {shelf.id} already exists in the library")
        
    def remove_shelf(self, shelf):
        if shelf in self.shelves:
            self.shelves.remove(shelf)
        else:
            print(f"Error: Shelf {shelf.id} does not exist in the library")
        
    def add_book(self, book, shelf):
        shelf.add_book(book)
        
    def remove_book(self, book, shelf):
        shelf.remove_book(book)
        
    def borrow_book(self, member, book):
        if book.status == "available":
            book.status = "borrowed"
            member.borrowed_books.append(book)
            print(f"{member.name} has borrowed {book.title} from the library")
        else:
            print("Book is not available currently")
            
    def return_book(self, member, book):
        if book.status == "borrowed":
            book.status = "available"
            member.borrowed_books.remove(book)
            print(f"{member.name} has returned {book.title} to the library")
        else:
            print("Book is not borrowed currently")
            
    def display_books(self):
        for shelf in self.shelves:
            shelf.display_books()
            
    def add_member(self, member):
        if member not in self.members:
            self.members.append(member)
            print(f"{member.name} has been added to the member database")
        else:
            print(f"Successfully added {member.name} to the member database")
        
    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
            print(f"Successfully removed {member.name} from the member database")
        
    def display_members(self):
        for member in self.members:
            book_count = len(member.borrowed_books)
            book_word = "book" if book_count == 1 else "books"
            print(f"{member.name} currently has {book_count} {book_word} borrowed")

def main():
    library = Library()
    shelfa1 = Shelf("A1")
    shelfc9 = Shelf("C9")
    library.add_shelf(shelfa1)
    library.add_shelf(shelfc9)
    
    book1 = Book("Book1", "Author1")
    book2 = Book("Book2", "Author2")
    member1 = Member("Alice", 1)
    member2 = Member("Bob", 2)
    
    library.add_book(book1, shelfa1)
    library.add_book(book2, shelfc9)
    
    library.add_member(member1)
    library.add_member(member2)
    
    library.borrow_book(member1, book1)
    library.borrow_book(member2, book2)
    
    library.display_books()
    library.display_members()
    
    library.return_book(member1, book1)
    
    library.display_books()
    library.display_members()
    
main()