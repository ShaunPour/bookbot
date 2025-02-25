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