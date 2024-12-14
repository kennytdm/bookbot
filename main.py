def charCount(text):
    chars = {}
    for c in text:
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def sortCharDictionary(dict):
    sortedList = []
    for c in dict:
        sortedList.append({"char": c, "num": dict[c]})
    sortedList.sort(key = sort_on_char)
    return sortedList

def sort_on_num(d):
    return d["num"]

def sort_on_char(d):
    return d["char"]
    

def main():

    with open("books/frankenstein.txt") as f:

        file_contents = f.read()
        
        words = file_contents.split()

        print(f"{len(words)} total words found")

        chars_dict = charCount(file_contents)

        sortedChars = sortCharDictionary(chars_dict)

        for pair in sortedChars:
            print(f"The '{pair['char']}' character was found {pair['num']} times")
    

main()