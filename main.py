def get_book_text(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            print(f"File Contents:\n {content}")
    except:
        print("Error. Filepath not found.")

def main():
    get_book_text("books/frankenstein.txt")

main()