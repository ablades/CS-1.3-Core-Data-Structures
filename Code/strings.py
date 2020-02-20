#!python


# def refactor(text, pattern, func):
#     """Refactor code to be dry"""
#     assert isinstance(text, str), 'text is not a string: {}'.format(text)
#     assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    
#     occurrences = []
#     for index, char in enumerate(text):

#         #Empty String Base
#         if pattern == '':
#             if func == 'contains':
#                 return True
#             elif func == 'find_index':
#                 return 0
#             elif func == 'find_all_indexes':
#                 occurrences.append(index)
#                 continue
        
#         #Potential Pattern
#         if char == pattern[0]:
#             j = index
#             #Compare to pattern
#             for letter in pattern:
#                 #Bounds checking
#                 if j > len(text) - 1 or text [j] != letter:
#                         break
#                 #Increment index
#                 j += 1
#             #matching substring
#             else:
#                 if func == 'contains':
#                     return True
#                 elif func == 'find_index':
#                     return index
#                 elif func == 'find_all_indexes':
#                     occurrences.append(index)
#     #Final returns
#     if func == 'contains':
#         return False
#     elif func == 'find_index':
#         return None
#     elif func == 'find_all_indexes':
#         return occurrences
                    
                        
    

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    
    if find_all_indexes(text, pattern) or pattern == '':
        return True
    else:
        return False
    # if pattern == '':
    #     return True

    # for index, char in enumerate(text):
    #     #look for matching first character
    #     if char == pattern[0]:
    #         #compare to pattern
    #         for letter in pattern:
    #             #
    #             if index > len(text) - 1 or text[index] != letter:
    #                 break
    #             #increment index
    #             index += 1
    #         #is a match
    #         else:
    #             return True

    # return False



def find_index(text, pattern, index=0):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    O(N*M) where n is length of text and M is the length of the pattern"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if pattern == '':
        return index
    
    while index < len(text):
        if text[index]  == pattern[0]:
            j = index
            for letter in pattern:
                if j > len(text) - 1 or text[j] != letter:
                    break
                j += 1
            else:
                return index

        index += 1
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    O(N*M) where n is length of text and M is the length of the pattern
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    

    occurrences = []
    i = 0
    while i < len(text):
        index = find_index(text,pattern, i)

        if index is not None:
            occurrences.append(index)
            i = index
        
        i += 1
    
        index = None
            
    return occurrences
    # for i, char in enumerate(text):
    #     #all characters are part of pattern
    #     if pattern == '':
    #         occurrences.append(i)
    #     #check characters against pattern
    #     elif char == pattern[0]:
    #         j = i
    #         for letter in pattern:
    #             #bounds and letter check
    #             if j > len(text) - 1 or  text[j] != letter:
    #                 break

    #             j += 1
    #         #pattern matches
    #         else:
    #             occurrences.append(i)

    # return occurrences


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
