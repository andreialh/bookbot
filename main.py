import sys
if len(sys.argv) < 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()
    

from stats import count_words, count_character, build_char_list, sort_on

def main():
    book = get_book_text(book_path)
    count = count_words(book)
    dictionary = count_character(book)
    char_list = build_char_list(dictionary)
    char_list.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in char_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    

main()
