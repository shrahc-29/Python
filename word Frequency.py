print("Python program that reads a block of text and creates a dictionary to store the frequency (count) of each word present in the text\n")

#Program to read a block of text and count word frequency

text = input("Enter a block of text:\n")    #Taking input of text
words = text.split()   #Splitting text into words

word_freq = {}    #dictionary to store word frequencies
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("\nWord Frequencies:")   #Printing results
for word in word_freq:
    print(word + ":", word_freq[word])
