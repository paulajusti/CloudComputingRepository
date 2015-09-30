phrase = input("Enter a phrase/word: ")

phrase = phrase.casefold()


rev_str = reversed(phrase)

if list(phrase) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")