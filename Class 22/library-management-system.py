class Book:
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.status = "available"
        
class Member:
    def __init__(self, name, id, borrowed_books):
        self.name = name
        self.id = id
        self.borrowed_books = []
        
class Library:
    def __init__(self, books, members):
        self.books = []
        self.members = []
        
    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} has been added to the library")
        
    def remove_book(self, book):
        self.books.remove(book)
        print(f"{book.title} has been removed from the library")
        
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
        for book in self.books:
            print(f"{book.title} by {book.author} is {book.status}")
            
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
    book1 = Book("Book1", "Author1", "available")
    book2 = Book("Book2", "Author2", "available")
    member1 = Member("Alice", 1, [])
    member2 = Member("Bob", 2, [])
    library = Library([], [])
    library.add_book(book1)
    library.add_book(book2)
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