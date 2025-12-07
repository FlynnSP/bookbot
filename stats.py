import sys

def count_words(text):
    num_of_words = len(text.split())
    return num_of_words

def count_letters(text):
    appeared = []
    letter_dict = {}
    splitted_text = text.split()
    joined_text = "".join(splitted_text)
    for letter in joined_text.lower():
        if letter not in appeared:
            letter_dict[letter] = 1
            appeared.append(letter)
        else:
            letter_dict[letter] += 1
    return letter_dict


def sort_on(items):
    return items["num"]


def write_report(text):
    letter_dict = count_letters(text)
    numwords = count_words(text)
    report_list = []
    
    for key, value in letter_dict.items():
        if key.isalpha():
            temp_dict = {}
            temp_dict["char"] = key
            temp_dict["num"] = value
            report_list.append(temp_dict)
    report_list.sort(reverse=True, key=sort_on)
    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {numwords} total words
--------- Character Count -------""")
    for pair in report_list:
        print(f"{pair["char"]}: {pair["num"]}")