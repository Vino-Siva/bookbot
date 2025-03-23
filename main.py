import sys
from stats import word_count, char_count, sort_list


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]


def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book


def main():
    file_string = get_book_text(path_to_book)
    num_words = word_count(file_string)
    character_counts = char_count(file_string)
    sorted_list = sort_list(character_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_list:
        print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")


main()
