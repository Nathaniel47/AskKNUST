import string
from pathlib import Path


file_path = Path(__file__).parent/"sacrifice_for_greatness.txt"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read().lower()


# removing punctuation
cleaned_text = text.translate(str.maketrans("", "", string.punctuation)).split()

count = {}

for word in cleaned_text:
    count[word] = count.get(word, 0) + 1

top_10_most_common = sorted(count.items(), key=lambda item: item[1], reverse=True)[:10]
print(top_10_most_common)
