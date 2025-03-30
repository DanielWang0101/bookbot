#input:filepath
#output: contents of the file as string
from stats import get_book_text
import sys
def main(fp):
    word_count, char_count, sorted_list = get_book_text(fp)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt..")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        print(f"{entry["name"]}: {entry["count"]}")
    print("============= END ===============")



# main("./books/frankenstein.txt")
if len(sys.argv)>1:
    main(sys.argv[1])
else:
    print("Please give the path to your book, for example typing in the command line: ")
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

