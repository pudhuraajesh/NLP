import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

def tokenize_text(text):
    return word_tokenize(text)

sample_inputs = [
    "Hello I am Raajesh",
    "B.Tech Artificial Intelligence and Data Science",
    "I am interested in Java"
]

for text in sample_inputs:
    print("Input Text:")
    print(text)
    print("Tokens:")
    print(tokenize_text(text))
    print("-" * 40)
