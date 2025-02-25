import sys
import os.path

def get_filepath():
    return sys.argv[1]

def get_book_content():
        filepath = sys.argv[1]
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        else:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

def word_count():
    content = get_book_content()
    word_list = content.split()
    txt_count = len(word_list)
    print(f"----------- Word Count ----------\nFound {txt_count} total words")


def char_count():
    char_list: dict[str, int] = {}
    words = list(get_book_content().lower())
    for char in words:
        if char in char_list:
            char_list[char] += 1
        else:
            char_list[char] = 1
    char_list_sorted = dict(sorted(char_list.items(), key=lambda x: x[1], reverse=True))

    return char_list_sorted