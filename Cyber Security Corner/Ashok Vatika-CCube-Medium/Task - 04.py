# Your code goes here

def xor_words(encrypted_text, key):
    result = ""
    for char1, char2 in zip(encrypted_txt, key):
        xor_value = ord(char1) ^ ord(char2)
        result += chr(xor_value)
    return result

# Example usage
encrypted_txt = "|OP`Z<E]|Y\$"
key = "Jai Shree Ram!"
result = xor_words(encrypted_txt, key)
print(result)

with open("location.txt", "w") as file:
    file.write(result)
