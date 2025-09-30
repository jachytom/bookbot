def get_book_text(fp):
    with open(fp) as f:
        return f.read()

# ***********************************************************

def get_num_words(fp):
    text = get_book_text(fp)
    return len(text.split())

# ***********************************************************

def get_character_count(fp):
    text = get_book_text(fp)
    dict = {} 
    for char in text:
        char = char.lower()
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

# ***********************************************************

def sort_on(items):
    return items["num"]

# ***********************************************************

def get_sorted_dict_list(fp):
    dict = get_character_count(fp)
    dict_list = []
    for key, value in dict.items():
        dict_list.append({'char': key, 'num': value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

# ***********************************************************

