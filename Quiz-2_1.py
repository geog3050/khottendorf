mystring=input('Please enter a string:')
letter=input('Please enter a letter:')
print(mystring,letter)
if letter in mystring:
    print('The character is in the string.')
else:
    print('The character is not in the string')