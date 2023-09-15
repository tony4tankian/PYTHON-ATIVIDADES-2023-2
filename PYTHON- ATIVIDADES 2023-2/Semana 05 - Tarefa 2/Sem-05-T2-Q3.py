caractere = input()

if caractere.isalpha() and caractere.lower() not in "aeiou":
    print(True)
else:
    print(False)