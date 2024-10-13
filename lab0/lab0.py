# Main class that will be involved 
class Book:
    def __init__(self, title: str, author: str, content: str):
        """Initializes a new instance of the Book class.
        
        Params
            title
                Title of the book.
            author
                Author of the book.
            content
                Content of the book.
        """
        self.title = title
        self.author = author
        self.content = content

    def get_summary(self) -> str:
        """Returns a summary of the book details.
        
        Return
            Summary of the book (title and author).
        """
        return f"'{self.title}' by {self.author}"

# Letter S: Single responsibility principle (SRP)

class BookPersistence:
    @staticmethod
    def save_to_file(book: Book, filename: str) -> None:
        """Saves the content of the book to a text file.
        
        Params 
            book
                An instance of the Book class.
            filename
                The name of the file where the book will be saved.
        """
        with open(filename, 'w') as file:
            file.write(f"Title: {book.title}\n")
            file.write(f"Author: {book.author}\n\n")
            file.write(book.content)

# Letter O: Open/Closed Principle (OCP)

class BookFormatter:
    @staticmethod
    def format_as_html(book: Book) -> str:
        """Formats the book's content as HTML.
        
        Params
            book
                An instance of the Book class.
        
        Return
            A string containing the book formatted as HTML.
        """
        return f"<html><head><title>{book.title}</title></head><body><h1>{book.title}</h1><h2>{book.author}</h2><p>{book.content}</p></body></html>"

    @staticmethod
    def format_as_json(book: Book) -> dict:
        """Formats the book's content as a JSON-like dictionary.
        
        Params
            book 
                An instance of the Book class.
        Return
            A dictionary containing the book's data.
        """
        return {
            "title": book.title,
            "author": book.author,
            "content": book.content
        }

# Example Usage
def main():
    # Create a new book instance
    my_book = Book("The Python Handbook", "John Doe", "This is a comprehensive guide to Python programming.")

    # Get a summary of the book
    print(my_book.get_summary())

    # Save the book to a text file
    BookPersistence.save_to_file(my_book, "my_book.txt")

    # Format the book as HTML and print it
    html_content = BookFormatter.format_as_html(my_book)
    print(html_content)

    # Format the book as JSON-like and print it
    json_content = BookFormatter.format_as_json(my_book)
    print(json_content)

if __name__ == "__main__":
    main()

# - The `Book` class follows SRP by only dealing with book data.
# - The `BookPersistence` class handles saving books, separating responsibilities.
# - The `BookFormatter` class extends the functionality of the `Book` class by adding formatting options, adhering to OCP.
# These demonstrate both the S (Single Responsibility) and O (Open/Closed) principles in action.