from collections import Counter

def word_count():
    try:
        filepath = 'books/frankenstein.txt'
        with open(filepath, 'r') as file:
                content = file.read()
        word_list = content.split()
        txt_count = len(word_list)
        print(f"{txt_count} words found in the document")
        return content
    except:
         print("Error. Filepath not found.")

def char_count():
    char_list = {}
    words = list(word_count().lower())
    for word in words:
         word_counts = words.count(word)
         char_list.update({word: word_counts})
         print(f"{word}: {word_counts}")