def word_count():
    try:
        filepath = 'books/frankenstein.txt'
        with open(filepath, 'r') as file:
                content = file.read()
        word_list = content.split()
        txt_count = len(word_list)
        print(f"{txt_count} words found in the document")
    except:
         print("Error. Filepath not found.")