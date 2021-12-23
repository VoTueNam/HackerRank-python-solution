ascii_array = []
def pangrams(string):
    lower_string = string.lower()
    for i in range(len(lower_string)):
        ascii_array.append(ord(lower_string[i]))
    for i in range(97, 123):
        if i not in ascii_array:
            return 'not pangram'
    return 'pangram'