from library.library import Library

def main():
    library = Library("City Library")

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Lists Books")
        print("3. Search Books")
        print("4. Add Member")
        print("5. List Members")
        print("6. Borrow Book")
        print("7. Return Book")
        print("0. Exit")

        choice = input("Enter choice: ").strip

        if choice == "1":
            book_id = int("Enter choice: ").strip
            title = input("Title: ")
            author = input("Author: ")
            qty = int(input("Quantity: "))
            library.add_book(book_id, title,author)
        
        elif choice == "2";
            for book in library.list_books():
                print(book)