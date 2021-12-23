def caesarCipher(text, s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        if text[i].isalpha():
            char = text[i]
     
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
     
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result+=text[i]
 
    return result


print(caesarCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 23))