from stats import word_count, char_count

def main():
    word_count()
    char_counts = char_count()
    for char, count in char_counts.items():
        char_counts = char_count()
    for char, count in char_counts.items():
        print(f"'{char}': {count}")
main()