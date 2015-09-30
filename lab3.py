phrase = input("Enter a string: ")

for (x=0; x<5;x++)
{
  if x=0
    phrase=Oxo
  if x=1
    phrase=OXO
  if x=2
    phrase=123454321
  if x=3
    phrase=ROTATOR
  if x=4
    phrase=12345	54321

  #helps in recognition of letters uppercase and lowercase
  phrase = phrase.casefold()

  rev_str = reversed(phrase)

  #method to revert the phrase and compare
  if list(phrase) == list(rev_str):
     print("It is palindrome")
  else:
     print("It is not palindrome. The phrase is not the same if you reverse it")
  X++
}