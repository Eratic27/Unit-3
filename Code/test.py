with open("10000 words.txt") as f:
    words = [word for line in f for word in line.split()]

print(words)