
def calc_val(word, key_word):
    value = 0
    #calculate value for each letter in word using ascii
    for char in word:
        if char in key_word:
            value += ord(char)

    return value



def read_words(input_list):
    #open dictonary
    with open("/usr/share/dict/words") as f:
        lines = f.read().lower()
        word_list = lines.split('\n')

    master_dictonary = dict()

    #read in all keywords
    for key_word in input_list:
        words = list()

        #loop through main dictionary
        for word in word_list:
            #calculate values and compare length of potential matches
            if len(word) == len(key_word) and calc_val(key_word, key_word) == calc_val(word, key_word):
                words.append(word)
        
        master_dictonary[key_word] = words

    return master_dictonary


if __name__ == "__main__":
    print(read_words(["tefon", "ogod","laisa", "laurr", "bureek", "prouot"]))
    # dict()
    # with open("/usr/share/dict/words") as f: 
    #     for line in f.readlines():
    #         print(len(str(line)))