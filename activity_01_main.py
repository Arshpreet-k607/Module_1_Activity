"""
Description: A client program written to verify correctness of 
the activity classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from genre.genre import Genre
from library_item.library_item import LibraryItem

def main():
    """
    Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    print("\n--- Creating LibraryItem with valid data ---")
    try:
        # 1. Create an instance of the LibraryItem class with valid inputs.
        item = LibraryItem(
            item_id=101,
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
            genre=Genre.FICTION,
            is_borrowed=False
        )
    except ValueError as e:
        print("Error creating LibraryItem:", e)
    else:
        # 2. Using the accessors, print each of the attributes.
        print(f"Item ID: {item.item_id}")
        print(f"Title: {item.title}")
        print(f"Author: {item.author}")
        print(f"Genre: {item.genre.name}")
        print(f"Is Borrowed: {item.is_borrowed}")

    print("\n--- Creating LibraryItem with invalid data ---")
    try:
        # 3. Create another instance with one or more invalid inputs (invalid genre and blank title).
        bad_item = LibraryItem(
            item_id="ABC",  # Invalid: not an int
            title="   ",    # Invalid: blank title
            author="Jane Doe",
            genre="Biography",  # Invalid: not in Genre enum
            is_borrowed="no"    # Invalid: not a bool
        )
    except ValueError as e:
        print("Error creating invalid LibraryItem:", e)

if __name__ == "__main__":
    main()
