# Program to sort alphabetically the words

my_srt = "Hello this Is an Example with Case letters"

my_srt = input("Enter a string: ")

# breakdown the srting into a list of words
words = my_srt.split()

# sort the list
words.sort()

# display the sorted words
print('The sorted words are: ')
for word in words:
    print(word)