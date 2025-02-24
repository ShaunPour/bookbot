def get_book_text(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
    except:
        print("Error. Filepath not found.")
    return content

def word_count():
    book_text = get_book_text("books/frankenstein.txt")
    word_list = book_text.split()
    txt_count = len(word_list)
    print(f"{txt_count} words found in the document")

def main():
    word_count()
main()