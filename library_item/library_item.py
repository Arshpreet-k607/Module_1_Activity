""""
Description: A class to manage LibraryItem objects.
"""
__author__ = "Arshpreet kaur"
__version__ = "1.0.0"

from genre.genre import Genre

class LibraryItem:
    """
    Represents a library item with ID, title, author, genre, and borrow status.
    """

    def __init__(self, item_id: int, title: str, author: str, genre: Genre, is_borrowed: bool):
        """
        Initializes a new LibraryItem.

        :param item_id: Unique ID for the item.
        :param title: The title of the library item.
        :param author: The author of the library item.
        :param genre: The genre of the library item.
        :param is_borrowed: Whether the item is borrowed.
        :raises ValueError: If any input is invalid.
        """
        title = title.strip()
        author = author.strip()

        if not isinstance(item_id, int):
            raise ValueError("Item Id must be numeric.")
        if not title:
            raise ValueError("Title cannot be blank.")
        if not author:
            raise ValueError("Author cannot be blank.")
        if not isinstance(genre, Genre):
            raise ValueError("Invalid Genre.")
        if not isinstance(is_borrowed, bool):
            raise ValueError("Is Borrowed must be a boolean value.")

        self.__item_id = item_id
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__is_borrowed = is_borrowed

    @property
    def item_id(self):
        """Returns the ID of the library item."""
        return self.__item_id

    @property
    def title(self):
        """Returns the title of the library item."""
        return self.__title

    @property
    def author(self):
        """Returns the author of the library item."""
        return self.__author

    @property
    def genre(self):
        """Returns the genre of the library item."""
        return self.__genre

    @property
    def is_borrowed(self):
        """Returns the borrowed status of the library item."""
        return self.__is_borrowed
