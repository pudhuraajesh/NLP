import re
def detect_word_pattern(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        print("Word patterns detected:")
        for match in matches:
            print(match)
    else:
        print("No word patterns detected.")

sample_inputs = [
    (r"\bfor\b", "Hello for Everyone"),
    (r"\b\d{4}\b", "I was born in the year of 2006"),
    (r"\b[a-zA-Z]{5}\b", "Hello,I am Raajesh"),
    (r"\bing\b", "Drinking Water is good for our body")
]

for pattern, text in sample_inputs:
    print("Pattern:", pattern)
    print("Text:", text)
    detect_word_pattern(pattern, text)

    print("-" * 40)
