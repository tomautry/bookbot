import sys
from stats import number_of_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath) as file:
        text = file.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    char_counts = count_characters(book_text)
    sorted_chars = sort_characters(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words(book_text)} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()