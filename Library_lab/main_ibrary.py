import json
from library import librarian

DATA_FILE = "library_data_file.json"


def load_library():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_library(library_data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(library_data, f, ensure_ascii=False, indent=2)


def show_menu():
    print("\nWelcome in library system\n")
    print("Select the service from the menu:")
    print("1- Add a book")
    print("2- Display all books")
    print("3- Search for books")
    print("4- Delete a book")
    print("5- Check out a book")
    print("6- Return a book")
    print("7- Exit")


def main():
    library_data = load_library()

    while True:
        show_menu()
        choice = input("please Choose from 1 to 7: ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            isbn = input("ISBN: ").strip()
            librarian.add_book(library_data, title, author, isbn)
            save_library(library_data)

        elif choice == "2":
            librarian.display_books(library_data)

        elif choice == "3":
            keyword = input("Search by keyword (title/author/isbn): ").strip()
            results = librarian.search_books(library_data, keyword)

            if not results:
                print("No matching books found.")
            else:
                for book in results:
                    status = "Available" if book["available"] else "Borrowed"
                    print(f'{book["title"]} by {book["author"]} (ISBN: {book["isbn"]}) - {status}')

        elif choice == "4":
            isbn = input("Enter ISBN to delete: ").strip()
            librarian.delete_book(library_data, isbn)
            save_library(library_data)

        elif choice == "5":
            isbn = input("Enter ISBN to borrow: ").strip()
            librarian.borrow_book(library_data, isbn)
            save_library(library_data)

        elif choice == "6":
            isbn = input("Enter ISBN to return: ").strip()
            librarian.return_book(library_data, isbn)
            save_library(library_data)

        elif choice == "7":
            print("Thank you for using our system.")
            break

        else:
            print("Invalid choice! please Choose number from 1 to 7.")


if __name__ == "__main__":
    main()