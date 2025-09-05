"""
Description: Unit tests for the LibraryItem class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_library_item.py
"""

__author__ = "Arshpreet Kaur"
__version__ = "1.0.0"

import unittest
from genre.genre import Genre
from library_item.library_item import LibraryItem

class TestLibraryItem(unittest.TestCase):

    def test_init_blank_title_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            LibraryItem(1, "   ", "Author", Genre.FICTION, False)
        self.assertEqual(str(context.exception), "Title cannot be blank.")

    def test_init_blank_author_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            LibraryItem(1, "Title", "   ", Genre.FICTION, False)
        self.assertEqual(str(context.exception), "Author cannot be blank.")

    def test_init_invalid_genre_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            LibraryItem(1, "Title", "Author", "Biography", False)
        self.assertEqual(str(context.exception), "Invalid Genre.")

    def test_init_invalid_item_id_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            LibraryItem("abc", "Title", "Author", Genre.FICTION, False)
        self.assertEqual(str(context.exception), "Item Id must be numeric.")

    def test_init_invalid_is_borrowed_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            LibraryItem(1, "Title", "Author", Genre.FICTION, "yes")
        self.assertEqual(str(context.exception), "Is Borrowed must be a boolean value.")

    def test_init_valid_sets_attributes(self):
        item = LibraryItem(1, "1984", "Orwell", Genre.FICTION, False)
        self.assertEqual(item._LibraryItem__item_id, 1)
        self.assertEqual(item._LibraryItem__title, "1984")
        self.assertEqual(item._LibraryItem__author, "Orwell")
        self.assertEqual(item._LibraryItem__genre, Genre.FICTION)
        self.assertEqual(item._LibraryItem__is_borrowed, False)

    def test_accessor_item_id(self):
        item = LibraryItem(2, "Book", "Author", Genre.FANTASY, True)
        self.assertEqual(item.item_id, 2)

    def test_accessor_title(self):
        item = LibraryItem(3, "Title", "Author", Genre.FICTION, False)
        self.assertEqual(item.title, "Title")

    def test_accessor_author(self):
        item = LibraryItem(4, "Title", "Author", Genre.FANTASY, True)
        self.assertEqual(item.author, "Author")

    def test_accessor_genre(self):
        item = LibraryItem(5, "Title", "Author", Genre.NON_FICTION, False)
        self.assertEqual(item.genre, Genre.NON_FICTION)

    def test_accessor_is_borrowed(self):
        item = LibraryItem(6, "Title", "Author", Genre.TRUE_CRIME, True)
        self.assertTrue(item.is_borrowed)

if __name__ == '__main__':
    unittest.main()
