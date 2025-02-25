from stats import word_count, char_count

def main():
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")
    word_count()
    char_counts = char_count()
    print("--------- Character Count -------")
    for char, count in char_counts.items():
        char_counts = char_count()
    for char, count in char_counts.items():
        print(f"{char}: {count}")
    print("============= END ===============")
main()