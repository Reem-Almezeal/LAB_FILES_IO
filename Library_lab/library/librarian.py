def add_book(library: dict, title: str, author: str, isbn: str):
    isbn = isbn.strip()
    if isbn in library:
        print(f"Book {isbn} already exists.")
        return

    library[isbn] = {
        "title": title.strip(),
        "author": author.strip(),
        "isbn": isbn,
        "available": True
    }
    print("Book added.")


def delete_book(library: dict, isbn: str):
    isbn = isbn.strip()
    if isbn not in library:
        print(f"Book {isbn} is not found.")
        return
    del library[isbn]
    print("Book deleted.")


def borrow_book(library: dict, isbn: str):
    isbn = isbn.strip()
    if isbn not in library:
        print(f"Book {isbn} is not found.")
        return
    if not library[isbn]["available"]:
        print(f"Book {isbn} already borrowed.")
        return

    library[isbn]["available"] = False
    print("Book checked out.")


def return_book(library: dict, isbn: str):
    isbn = isbn.strip()
    if isbn not in library:
        print(f"Book {isbn} is not found.")
        return
    library[isbn]["available"] = True
    print("Book returned.")


def display_books(library: dict):
    if not library:
        print("There are no books.")
        return

    for isbn, b in library.items():
        status = "Available" if b["available"] else "Borrowed"
        print(f'{b["title"]} by {b["author"]} (ISBN: {isbn}) - {status}')

def search_books(library: dict, keyword: str):
    keyword = keyword.strip().lower()
    results = []

    for isbn, b in library.items():
        if (keyword in isbn.lower()
                or keyword in b["title"].lower()
                or keyword in b["author"].lower()):
            results.append(b)

    return results