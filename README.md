# Intermediate Software Development Activity 1

This activity is designed to reinforce key concepts introduced in Module 1, including:

- Interpreting a Class Diagram to understand system design
- Applying Encapsulation principles to protect data within classes
- Creating and working with Classes in Python
- Planning and implementing Unit Tests to ensure code correctness

---

## Objectives

By completing this activity, you will:

- Interpret a UML class diagram to implement corresponding Python classes.
- Implement private attributes and public accessors to enforce encapsulation.
- Validate input data and handle exceptions appropriately.
- Write unit tests using Python’s `unittest` framework.
- Use a client program to demonstrate the functionality of your classes.

---

## Project Structure

- `genre/` - Contains the `Genre` enumeration class.
- `library_item/` - Contains the `LibraryItem` class representing items in a library.
- `tests/` - Contains unit tests for your classes and a test plan file.
- `activity_01_main.py` - A client program to verify your implementation.
- `.gitignore` - Git configuration file.
- `README.md` - This documentation file.

---

## How to Use

1. **Implement your classes** in the appropriate directories based on the class diagram.
2. **Run unit tests** to validate your implementation:
   ```bash
   python -m unittest tests/test_library_item.py

## Author
- Arshpreet Kaur

## Additional Information

- Be sure to include comprehensive docstrings for all classes and methods.

- Follow Python’s PEP 8 style guidelines.

- Validate inputs carefully and raise exceptions with descriptive messages.

- Use this project to strengthen your understanding of object-oriented design and testing    principles.

- Feel free to extend the functionality or add new tests for further practice.