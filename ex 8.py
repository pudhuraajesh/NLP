import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
sentence = input("Enter a sentence: ")
words = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(words)
print("\nPOS Tags:\n", pos_tags)
grammar = r"""
    NP: {<DT>?<JJ>*<NN>+}
"""
chunk_parser = nltk.RegexpParser(grammar)
chunk_tree = chunk_parser.parse(pos_tags)
print("\nChunk Tree:")
print(chunk_tree)
try:
    chunk_tree.draw()
except:
    print("\nTree visualization not supported (Tkinter not installed).")
