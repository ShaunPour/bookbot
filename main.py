from stats import word_count, char_count, get_filepath

def main():
    filepath = get_filepath()
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...")
    word_count()
    char_counts = char_count()
    print("--------- Character Count -------")
    for char, count in char_counts.items():
        char_counts = char_count()
    for char, count in char_counts.items():
        print(f"{char}: {count}")
    print("============= END ===============")
main()