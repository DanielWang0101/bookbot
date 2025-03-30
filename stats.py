def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

        #count words
        return count_words(file_contents), char_count(file_contents), convert_to_sorted_list(char_count(file_contents))

def count_words(file_content_string):
    return len(file_content_string.split())

# @ input string
# @ output character count of each charater unique appeared
def char_count(file_contents):
    if type(file_contents) != str:
        return type(file_contents)
    result = {}
    file_contents = file_contents.lower()
    for char in file_contents:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    
    
    return result

def convert_to_sorted_list(dic):
    result = []
    for key in dic:
        if key.isalpha() == True:
            entry = {}
            entry["name"] = key
            entry["count"] = dic[key]
            result.append(entry)
    def sort_on(dict):
        return dict["count"]
    
    result.sort(reverse=True, key=sort_on)
    return result