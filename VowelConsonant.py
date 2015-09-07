userInput = input("Enter your sentance: ")
vowels="AEIOUaeiou"


displayVowels=""
displayConsonants=""

for letter in userInput:
    if letter in vowels:
        dislpayVowels = displayVowels = letter
    else:
        displayConsonants = displayConsonants + letter


print("Consonants: " +displayConsonants)
print("vowels: " + displayVowels)
