from stats import get_num_words, get_character_count, get_sorted_dict_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
file_path = sys.argv[1]


header = f'''============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------'''
print(header)
print(f"Found {get_num_words(file_path)} total words")
print("--------- Character Count -------")
for dict in get_sorted_dict_list(file_path):
    if dict["char"].isalpha():
        print(dict["char"] + ": " + str(dict["num"]))
print("============= END ===============")
