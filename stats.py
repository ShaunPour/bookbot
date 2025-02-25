def get_book_content():
    try:
        filepath = 'books/frankenstein.txt'
        with open(filepath, 'r') as file:
            return file.read()
    except:
        print("Error. Filepath not found.")

def word_count():
    content = get_book_content()
    word_list = content.split()
    txt_count = len(word_list)
    print(f"{txt_count} words found in the document")


def char_count():
    char_list = {}
    words = list(get_book_content().lower())
    for char in words:
        if char in char_list:
            char_list[char] += 1
        else:
            char_list[char] = 1
    return char_list