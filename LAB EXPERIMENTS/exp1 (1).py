import re

text = input("Enter a sentence: ")
pattern = input("Enter the word to search: ")

result = re.search(pattern, text)

if result:
    print("Pattern found.")
else:
    print("Pattern not found.")