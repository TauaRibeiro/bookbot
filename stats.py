def get_num_words(words: list[str]) -> int:
    return len(words)

def get_num_characters(book: str) -> dict:
    result = dict()
    book = book.lower()

    for character in book:
        if not character in result.keys():
            result[character] = 1
        else:
            result[character] += 1

    return result 

def order_dict(dictionary: dict) -> list:
    list_items = list()

    def order_key(d: dict):
        for num in d.values():
            return num
    
    for key, value in dictionary.items():
        list_items.append({key: value})
    
    list_items.sort(reverse= True, key= order_key)
    
    return list_items

