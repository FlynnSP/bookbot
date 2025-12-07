from stats import count_words, count_letters, write_report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text


def main():
    if len(sys.argv) != 2:
        print("\n\nUsage: python3 main.py <path_to_book>\n\n")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    count_words(text) 
    #count_letters(text)
    write_report(text)  
print(sys.argv)

main()