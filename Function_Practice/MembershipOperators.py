# membershipOperators = test value variable found in sequence
# (String, list,tuple,set,dictionary)

#1. in
#2. not in

word = "APPLE"
letter  = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")


email ="m.aftabafridi@gmail.com"

if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email")
