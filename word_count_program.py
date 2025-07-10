
'''
📌 Input: A sentence
📌 Output: Number of times each word appears
'''

sentence = "hello world hello python world python python"

words = sentence.split()
word_count = {}

for word in words :
    word_count[word] = word_count.get(word, 0) + 1

print("Word count: ")
for word, count in word_count.items():               # Logic --> (key, value) = (word, count)
    print(f"{word}: {count}")