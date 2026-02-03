from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print("Enter words separated by space:")
text = input()
words = text.split()
stemmed_words = [stemmer.stem(word) for word in words]
print("\nOriginal Words:")
print(words)
print("\nStemmed Words:")
print(stemmed_words)
