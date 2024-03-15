def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

result = reverse_words("Hello, World!")
print(result)