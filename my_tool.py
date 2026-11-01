# my_tool.py
# Author: Syan Patel


class BookLookup:
    """A tool that knows which books are on the shelf. It knows nothing about chatting."""

    def __init__(self, books):
        """Store a dictionary that maps a book title (lowercase) to copies on the shelf."""
        self.books = books

    def find_title(self, text):
        """Return the first known book title mentioned in text, or None."""
        for title in self.books:
            if title in text.lower():
                return title
        return None

    def copies_for(self, title):
        """Return how many copies are on the shelf, or None if the library does not have it."""
        if title in self.books:
            return self.books[title]
        return None
