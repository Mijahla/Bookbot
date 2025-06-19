def count_words(file_contents):
    """Count the number of words in text."""
    return len(file_contents.split())

def count_chars(file_contents):
    """Count occurrences of each alphabetical character (case-insensitive)."""
    file_contents = file_contents.lower()
    char_counts = {}
    for char in file_contents:
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_on(char_dict):
    """Key function for sorting by character count."""
    return char_dict["count"]

def get_sorted_char_counts(file_contents):
    """Return sorted list of character counts."""
    char_counts = count_chars(file_contents)
    sorted_list = [{"char": char, "count": count} for char, count in char_counts.items()]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

