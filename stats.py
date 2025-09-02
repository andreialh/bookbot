def count_words(text):
    words = text.split()
    words_count = len(words)
    return words_count

def count_character(book_text):
    lowercase_character = book_text.lower()
    character_dict = {}
    for character in lowercase_character:
        character_dict[character] = character_dict.get(character, 0) + 1
    return character_dict

def build_char_list(counts):
    new_list = []
    for key, value in counts.items():
        if key.isalpha():
            entry = {"char": key, "num": value} 
            new_list.append(entry)       
    return new_list

def sort_on(items):
    return items["num"]



