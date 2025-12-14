# Chef and the ancient jungle monkeys
n = int(input())
words = []

# take all the word and put it to a words list
for i in range(n):
    word = input()
    words.append(word)
# verify words and print it with 'oi'
for word in words:
    if word.endswith("us"): # handle case if word ends with 'us' or not
        root = word[:-2] # slice it and remove 'us'
        new_word = root + "oi" # add 'oi' to the root
        print(new_word)
    else:
        print(word)
