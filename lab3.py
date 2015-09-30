phrase = input("Enter a string: ")

#helps in recognition of letters uppercase and lowercase
phrase = phrase.casefold()


rev_str = reversed(phrase)

if list(phrase) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")