# =========== წიგნების მართვის კონსოლ აპლიკაცია ==================

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"title: {self.title}, author: {self.author}, year: {self.year}"


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("\n The book has been added successfully!")

    def list_books(self):
        if not self.books:
            print("\n No books available.")
            return
        print("\n List of books:")
        for book in self.books:
            print(book)

    def search_by_title(self, title):
        found = [book for book in self.books if book.title.lower() == title.lower()]
        return found


def get_valid_year():
    while True:
        year = input("Year of Publication: ")
        if year.isdigit() and 0 < int(year) <= 2025:
            return int(year)
        else:
            print(" Please enter a valid year!")



def main():
    manager = BookManager()

    while True:
        print("\n=== Book Management Platform ===")
        print("1. Add new book")
        print("2. All available books")
        print("3. Search by title")
        print("4. Exit")
        print("=" * 20)
        choice = input("Please select an option: ")

        if choice == "1":
            print("\n Add new book")
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            year = get_valid_year()

            if title and author:
                manager.add_book(Book(title, author, year))
            else:
                print(" All field are necessary!")

        elif choice == "2":
            manager.list_books()

        elif choice == "3":
            title = input("\nEnter the book title: ").strip()
            results = manager.search_by_title(title)
            if results:
                print("\n Found books:")
                for book in results:
                    print(book)
            else:
                print("\n No books available with this title.")

        elif choice == "4":
            print("\nThanks for using our Platform! ")
            break

        else:
            print(" Please enter the correct option (1–4)!")



if __name__ == "__main__":
    main()


# title: Great Expectations, author: Charles Dickens, year: 1861
# title: White Fang, author: Jack London, year: 1906
# title: 1984, author: George Orwell, year: 1949
# title: The Lord of the Rings, author: J. R. R. Tolkien, year: 1954
# title: კაცია-ადამიანი, author: Ilia Chavchavadze, year: 1863
# title: Oliver Twist, author: Charles Dickens, year: 1838