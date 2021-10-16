from script.phone import PhoneNumber

keypad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


def get_letters(digits, alphabet):
    """
    Select the associated letter to each
    number and return a string of letters.
    :param digits: a string containing numbers eg. "3"
    :param alphabet: a dictionary eg. {'2': 'abc', '3': 'def'}
    :return: a string containing different letters eg. 'def'
    This is the doctest:
    >>> get_letters("3",{'2': 'abc', '3': 'def'})
    'def'
    """
    return "".join([value for key, value in alphabet.items() if key in digits])


def check_correspondence(word_list, letters):
    """
    Check for each word of word_list if each letter is contained
    in 'letters'.
    :param word_list: eg. ["foo", "bar", "baz"]
    :param letters: eg. "efghij"
    :return: return an array of each word meeting the above condition
    This is the doctest:
    >>> check_correspondence(["foo", "bar", "baz"],"efo")
    ['foo']
    """
    return [word for word in word_list if contains_all(remove_duplicate_char(word), set(letters))]


def remove_duplicate_char(string):
    """
    Remove duplicate character from a string
    :param string: a simple word (eg "aabacab")
    :return: a string without duplicate character (eg. "abc")
    This is the doctest:
    """
    return "".join(set(string))


def contains_all(string, set_letter):
    """
    Check whether all characters in str contained in set.
    :param string: eg. "foo"
    :param set_letter: eg. {"f","o","s}
    :return: a boolean eg. True
    This is the doctest:
    >>> contains_all("foo", {"f","o","s"})
    True
    """
    return all(c in set_letter for c in string)


def sanatise_array(string):
    """
    Adapt the format of the input eg. ["foo", "bar", "baz"]
    """
    for i in ' "[]':
        string = string.replace(i, "")
    return string.split(",")


def solver(phone_number, word_list, keypad_dict):
    """
    Given a phone_number of length n and a list of words (word_list), return a list of only the words where each
    letter of that word corresponds to a number in the phone number.
    :param phone_number: a string containing numbers eg. "3662277"
    :param word_list: an array of strings eg. ["foo", "bar", "baz"]
    :param keypad_dict: a dictionary eg. {'2': 'abc', '3': 'def', ...}
    :return: an array eg. ["foo", "bar"]
    This is the doctest:
    >>> solver(phone_number="3662277", word_list=["foo", "bar", "baz"], keypad_dict=keypad)
    ['foo', 'bar']
    """
    phone_number = PhoneNumber(phone_number)
    letters = get_letters(phone_number.get_digits(), keypad_dict)
    return check_correspondence(word_list, letters)
