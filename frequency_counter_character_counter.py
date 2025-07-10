
# 📌 Input: A string
# 📌 Output: Frequency of each character

text = "banana"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character Frequencies:")    
for char, count in frequency.items():              # Logic --> (key, value) = (word, count)
    print(f"{char} : {count}")