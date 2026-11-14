# Q24) Problem statement: Write a program to count the vowels in a given string.
# Consider both uppercase and lowercase vowels.

# Write a program to count the vowels in a given string. Consider both uppercase and lowercase vowels.

s = input("Enter a string: ")

count = 0
for ch in s.lower():
    if ch in "aeiou":
        count += 1

print(f"{count} vowel" if count == 1 else f"{count} vowels")
