import sys

from stats import get_num_words, get_num_characters, order_dict


try:
    PATH = sys.argv[1]
except:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def get_book_text(path: str):
    with open(path) as f:
        content = f.read()

        return content

def main():
    book = get_book_text(PATH)
    num_characters = get_num_characters(book)

    print(f"{' BOOKBOT ':=^30}")
    
    print(f"{' Worls Count ':-^30}")
    print(f'Found {get_num_words(book.split())} total words')
    
    print(f"{' Character Count ':-^30}")
    for dict in order_dict(num_characters):
        for char in dict.keys():
            if char.isalpha():
                print(f"{char}: {dict[char]}")
    
    print(f"{' END ':=^30}")

main()