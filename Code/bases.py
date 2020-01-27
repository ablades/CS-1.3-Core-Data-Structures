import string

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    #Reverse digit order
    digits = digits[::-1]
    decoded_val = 0

    for exp, digit in enumerate(digits):
        #Value of current power with given base and expontent
        pow_val = pow(base, exp)

        #is a hex character 97(a)
        if digit.isalpha():
            digit = digit.lower()
            digit = ord(digit) - 97 + 10
        else:
            digit = int(digit)

        decoded_val += digit * pow_val

    return decoded_val

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    encoded_val = ""
    
    while number > 0:
        #Modulo always returns a value less than the base
        number, remainder = divmod(number, base)
        
        #convert numbers 10 or higher to letters
        if remainder >= 10:
            encoded_val += chr(remainder + 87)
        else:
            encoded_val += str(remainder)

    return encoded_val[::-1]


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    #decode values to base 10 then encode to any base
    base10_val = decode(digits, base1)

    return encode(base10_val, base2)

#Stretch Challenges 
def radix_convert(number, base):
    """Convert number in base 10 to digits in given base.
    number: float -- float representation of number (in base 10)
    base: int -- the base to convert to
    return: str -- string representation of number (in given base)"""
    #get only decimal value
    decimal_val = number % 1

    #truncate number
    number = int(number)
    #value 
    val = encode(number, base) + "."

    #continue until decimal begins to repeat
    repeat_val = decimal_val
    while True:
        result = decimal_val * base
        print(result)
        #truncate result
        val += str(int(result))
        print(val)
        #keep decimal of result
        decimal_val = result % 1
        print(decimal_val)
        print("-----------")
        if decimal_val == repeat_val or decimal_val == .0:
            break

    return val





def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')
        radix_convert(12.3125, 2)


if __name__ == '__main__':
    main()
