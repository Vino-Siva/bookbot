import string


def word_count(file_string):
    words = file_string.split()
    return len(words)


def char_count(file_string):
    char_dict = {}
    letters = list(string.ascii_lowercase)
    letters.extend(["æ", "â", "ê", "ë", "ô"])
    convert_lower = file_string.lower()
    for letter in letters:
        char_dict[letter] = convert_lower.count(letter)
    return char_dict


def sort_list(dict):
    dict_list = []
    for key, value in dict.items():
        new_item = {"char": key, "num": value}
        dict_list.append(new_item)

    def sort_on(dict):
        return dict["num"]
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
