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

    def add_book(self, book, color_list):
        try:
            duplicate_books = any(book.title == b.title and book.author == b.author for b in self.books)
            if not duplicate_books:
                self.books.append(book)
                print("\n***** THE BOOK HAS BEEN ADDED SUCCESSFULLY! *****")
            else:
                print(f"\n***** THE BOOK WITH THE TITLE '{color_list[0]}{book.title}{color_list[1]}' AND AUTHOR '{color_list[0]}{book.author}{color_list[1]}' IS ALREADY ADDED! *****")
        except Exception as e:
            print(f"\n***** BOOK ADDITION HAS FAILED! *****")
            print(e)

    def list_books(self, color_list):
        if not self.books:
            print("\n***** NO BOOK AVAILABLE! ******")
            return
        format_output()
        for book in self.books:
            print(f"{color_list[0]}{book.title:<25}{book.author:^25}{book.year:^15}{color_list[1]}")
            print('-' * 65)

    def search_by_title(self, title):
        found = [book for book in self.books if book.title.lower() == title.lower()]
        return found


def get_valid_year():
    while True:
        year = input("Year of Publication: ")
        if year.isdigit() and 0 < int(year) <= 2025:
            return int(year)
        else:
            print("\n***** PLEASE ENTER A VALID YEAR! *****")


def get_valid_field(title, author):
    if title and author:
        return title and author
    print("\n***** ALL FIELDS ARE NECESSARY! *****")


def format_output():
    print(f"{'TITLE':<25}{'AUTHOR':^25}{'YEAR':^15}")
    print("#" * 65)


def main():
    green = "\033[32m"
    reset = "\033[0m"
    color_list = [green, reset]
    manager = BookManager()

    while True:
        print(f"\n\n\n===== BOOK MANAGEMENT PLATFORM =====\n")
        print("1. Add new book")
        print("2. All available books")
        print("3. Search by title")
        print("4. Exit")
        print("=" * 40)
        choice = input("Please select an option: ")
        print()
        if choice == "1":
            print("\n***** ADD NEW BOOK *****\n")
            # title = input("Title: ").strip()
            # author = input("Author: ").strip()
            # year = get_valid_year()
            # if get_valid_field(title, author):
            #     manager.add_book(Book(title, author, year))

            book_1 = Book(title='Great Expectations', author='Charles Dickens', year=1861)
            book_2 = Book(title='White Fang', author='Jack London', year=1906)
            book_3 = Book(title='1984', author='George Orwell', year=1949)
            book_4 = Book(title='The Lord of the Rings', author='J. R. R. Tolkien', year=1954)
            book_5 = Book(title='კაცია-ადამიანი', author='Ilia Chavchavadze', year=1863)
            book_6 = Book(title='Oliver Twist', author='Charles Dickens', year=1838)
            book_7 = Book(title='White Fang', author='Jack London', year=1906)
            book_list = [book_1, book_2, book_3, book_4, book_6, book_7]
            for i in book_list:
                if get_valid_field(i.title, i.author):
                    manager.add_book(i, color_list)

        elif choice == "2":
            manager.list_books(color_list)

        elif choice == "3":
            title = input("\nEnter the book title: ").strip()
            results = manager.search_by_title(title)
            if results:
                print("\n***** FOUND BOOKS: *****\n")
                format_output()
                for book in results:
                    print(f"{color_list[0]}{book.title:<25}{book.author:^25}{book.year:^15}{color_list[1]}")
            else:
                print("\n***** NO BOOK AVAILABLE WITH THIS TITLE! *****")

        elif choice == "4":
            print("\n***** THANKS FOR USING OUR PLATFORM! *****")
            break

        else:
            print("Please enter the correct option (1–4)!")


if __name__ == "__main__":
    main()
