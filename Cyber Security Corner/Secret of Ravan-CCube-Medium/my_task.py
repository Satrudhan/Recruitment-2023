
# characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', ';', ':', '"', "'", '<', '>', '?', ',', '.', '/', '`', '~']
# known_password_dict = {'n':1, '_':2, '^':3, '`':5, 'W':6, '5':8}

# As you can see, characters at 4th and 7th position are missing. You need to find those characters using brute-force.



# Write your code here
def save_combinations_to_file(chars, filename):
    with open(filename, 'w') as file:
        for i in range(len(chars)):
            for j in range(len(chars)):
                combination = chars[i] + chars[j]
                file.write(combination + '\n')

# Example usage
char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', ';', ':', '"', "'", '<', '>', '?', ',', '.', '/', '`', '~']
output_file = 'combinations.txt'
save_combinations_to_file(char_list, output_file)
print("Combinations saved to", output_file)



with open('combinations.txt', 'r') as input_file:
    with open('poss_pass.txt', 'w') as output_file:
        for line in input_file:
            line = line.strip()  # Remove leading/trailing whitespace
            if len(line) >= 2:
                modified_line = 'n' + '_^' + line[0] + '`W' + line[1] + '5 '
                output_file.write(modified_line + '\n')


import pyzipper

wordlist = "poss_pass.txt"
file = "The_secret.zip"
extract_path = "./extracted_files/"

with open(wordlist, "r") as wordlist_file:
    for password in wordlist_file:
        try:
            with pyzipper.AESZipFile(file) as zip_file:
                zip_file.extractall(extract_path, pwd=password.strip().encode())
        except RuntimeError:
            print("Trying password:", password.strip())
            continue
        else:
            print("Password found:", password.strip())
            break
    else:
        print("No password matches, try another list")
