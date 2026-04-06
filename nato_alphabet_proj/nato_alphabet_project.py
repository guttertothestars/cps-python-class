import json  # json library for handling json data

with open("nato_alphabet.json", "r") as file:
    nato_alphabet = json.load(file)

print("I can translate letters into the NATO alphabet")
print("I can only handle alphabet letters and numbers.")
print("All other characters will be ignored.")
print('If you are done with translations simply type "*".')

# set an empty string
string_to_translate = ""

while True:
    string_to_translate = input("What would you like to translate today?: ").lower()
    if string_to_translate == "*":
        break

    chars = list(string_to_translate)

    translated_chars = []
    for char in chars:
        if char in nato_alphabet:
            translated_chars.append(nato_alphabet[char].capitalize())

    translated_string = " ".join(translated_chars)
    print("Say: ", translated_string)

print("Thank you for using my program.")
print("Goodbye")
