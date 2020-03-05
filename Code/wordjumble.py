
def calc_val(word):
    value = 0
    #calculate value for each letter in word using ascii
    for char in word:
        value += ord(char) - 96

    return value

def build_dict(words):
    word_dict = {}

    for word in words:
        word_dict[word] = read_words(word)

    return word_dict



def read_words(key_word):

    with open("/usr/share/dict/words") as f:
        lines = f.read().lower()

    word_list = lines.split('\n')
    words = list()
    
    for word in word_list:
        if len(word) == len(key_word) and calc_val(key_word) == calc_val(word):
            words.append(word)

    return words


if __name__ == "__main__":
    read_words("tefon")
    print(build_dict(['tefon']))
    # dict()
    # with open("/usr/share/dict/words") as f: 
    #     for line in f.readlines():
    #         print(len(str(line)))