def number_of_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    return len(text)

def count_characters(text):
    char_dict = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def sort_characters(char_dict):
    def sort_by_count(item):
        return item["num"]
    
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    char_list.sort(key=sort_by_count, reverse=True)
    return char_list
