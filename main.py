from stats import count_words, get_sorted_char_counts
import sys

def main():
    """Generate book analysis report."""
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
    #if len(sys.argv)!=2:
     #   print("Usage: python3 main.py <path_to_book>")
    

    with open(file_path, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    sorted_chars = get_sorted_char_counts(file_contents)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")  # Format with thousands separator
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['count']}")


if __name__ == "__main__":
    main()
