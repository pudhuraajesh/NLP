import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
def pos_tagging_tool():
    print("--- NLP POS Tagging Tool ---")
    print("Type 'exit' to quit.\n")
    while True:
        text = input("Enter a sentence: ").strip()
        if text.lower() == 'exit':
            break
        if not text:
            continue
        tokens = word_tokenize(text)
        tags = nltk.pos_tag(tokens)
        print("\nTagged Output:")
        print(tags)
        print("\nBreakdown:")
        for word, tag in tags:
            print(f"Word: {word:<12} | Tag: {tag}")
        print("-" * 40)
if __name__ == "__main__":
    pos_tagging_tool()
