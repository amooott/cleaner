----------------------------------
Text Cleaner Script
----------------------------------

------------
Description
------------

This Python script helps clean .txt files by removing unwanted words, phrases, or lines. It’s perfect for quickly removing repetitive or undesired text.
Features

    Lists all .txt files in the current directory.
    Allows users to specify words or phrases to delete.
    Removes lines starting with specific patterns (e.g., emoji).
    Provides feedback on how many occurrences and lines were deleted.
    Simple error handling for invalid inputs.
------
Usage
------
    Save the script (e.g., text_cleaner.py) in the directory with .txt files.
    Run the script:

    python text_cleaner.py

    Follow the prompts to select a file and enter words/phrases to delete.

Example

Input File:


    Hello 🌍 world!
    This is a test message.
    Please remove "test" and "world".


After cleaning with patterns test, world:

    Hello 🌍 !
    This is a message.

Enjoy !
