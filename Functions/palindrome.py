def palindrome(word):
    rev = word[::-1]
    if rev == word:
        print(f'{word} is a palindrom.')
    else:
        print(f'{word} is not a palindrom.')

# simplest palindrom function
def palindrom1(word):
    return word == word[::-1]
    
word = input("Enter the word to check if it is palindrom: ")

palindrome(word)
print(palindrom1(word))
    