# Name: Jamaica C. Palillo
# Section: BSCPE 1-5

# Exercise 4: Remove first n characters from a string


input_word = str (input ("Enter a word: "))
n = int (input ("How many characters do you want to remove? "))

def remove_characters (input_word, n):
    if n > len(input_word):
        return "Invalid. 'n' must be less than the length of the string."
    else:
        result =input_word [n:]
        return result

result = remove_characters (input_word, n)
print (result)