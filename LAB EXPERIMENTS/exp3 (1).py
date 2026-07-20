from nltk.stem import PorterStemmer

ps = PorterStemmer()

word = input("Enter a word: ")

stem = ps.stem(word)

print("Stem:", stem)
