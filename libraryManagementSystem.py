class LibraryManagementSystem:
    def __init__(self):
        self.books = []


    def add_book(self, title, author, copies):
        d = {"title":title, "author":author, "avialable_copies":copies,"original_copies":copies}
        self.books.append(d)
        print(f"{title} book is added successfully!!")

    def display_book(self):
        if self.books:
            #show the books
            for book in self.books:
                print(f"The book title: {book['title']} | author: {book['author']} | available Copies {book['avialable_copies']} | original copy: {book['original_copies']}")
        else:
            print("No books are available!!")

    def helper_func(self,title):
        if self.books:
            for book in self.books:
                if book['title'].lower() == title.lower():
                    return book
        else:
            return None
    def borrow_book(self, title):
        #it check if book avaialable or not
        book = self.helper_func(title)
        if book:
            if book['avialable_copies'] > 0:
                book['avialable_copies'] -= 1
                print(f" {book['title']} has been borrowed successfully!!")
            else:
                print("No stock! No copies available!")

    def return_book(self,title):
        #check its our library book
        book = self.helper_func(title)
        if book:
            if book['avialable_copies'] < book['original_copies']:
                book['avialable_copies'] += 1
                print(f"{book['title']} has retured successfully!!")
            else:
                print("Sorry!, may be this book not belongs to us!")
        else:
            print("This book not belongs to our library!!")


obj = LibraryManagementSystem()
obj.display_book()
obj.add_book("The life in qatar","Ahmed",5)

obj.add_book("The python programming","KAIF",3)
obj.display_book()
obj.borrow_book("The life in qatar")
obj.display_book()
obj.borrow_book("The life in qatar")
obj.display_book()
obj.return_book("The life in qatar")
obj.display_book()

obj.return_book("The life in qatar")
obj.display_book()


obj.return_book("The life in qatar")
obj.display_book()