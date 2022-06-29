def translate(s):
    translation = ""
    for letter in s:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else :
            translation = translation + letter
    return translation
s = input()
print(translate(s))