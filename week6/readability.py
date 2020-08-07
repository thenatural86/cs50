from cs50 import get_string

string = get_string("Text: ")
letters = words = sentences = 0
for i in range(len(string)):
    if string[i].isalpha():
        # print(i, string[i].isalpha())
        letters += 1
    if i == 0 and string[i] != " " or i != len(string) - 1 and string[i] == " " and string[i + 1] != " ":
        words += 1
    if string[i] == "!" or string[i] == "." or string[i] == "?":
        sentences += 1
# print(letters)
# print(words)
# print(sentences)

L = (letters / words) * 100
S = (sentences / words) * 100
index = round(0.0588 * L - 0.296 * S - 15.8)
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
# print(L, S, index)

    #   for char in s:
    # print(char, char.isalpha())
