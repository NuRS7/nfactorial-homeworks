# Exercise 5: is-vowel
# Declare a character
# Check if the character is a vowel
# Print the result

# char = input('')
# Input қалдырдым тоже жұмыс жасай береді
char = 'a'
if char.lower() in 'aeiou': # lower бердім себебі үлкен әріппен жазғанда жасамай қалады екен код
	print(f'{char} is Vowel')
else:
	print(f'{char} is not Vowel')