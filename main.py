from phone import PhoneNumber

keypad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

def get_letters(digits, alphabet):
    """
    Select the associated letter to each
    number and return a string of letters.
    """
    return "".join([value for key, value in alphabet.items() if key in digits])


def check_correspondence(word_list, letters):
    """
    Check for each word of word_list ( eg. ["foo", "bar", "baz"]) if each letter is contained
    in 'letters' (eg. "efghij").
    """
    return [word for word in word_list if containsAll(word, set(letters))]


def containsAll(str, set):
    """ Check whether all characters in str contained in set. """
    return all(c in set for c in str)


def solver(phone_number, word_list, keypad_dict):
    """
    Given a phone_number of length n and a list of words (word_list), return a list of only the words where each
    letter of that word corresponds to a number in the phone number. """
    phone_number = PhoneNumber(phone_number)
    letters = get_letters(phone_number.get_digits(), keypad_dict)
    return check_correspondence(word_list, letters)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solver(phone_number="3662277", word_list=["foo", "bar", "baz"], keypad_dict=keypad))

