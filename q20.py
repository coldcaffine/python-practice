# Q20) Problem statement: Accept a sentence and a word. Use the find() method to
# determine the starting index of the word. Display a message if the word is not
# found.

# Accept a sentence and a word. Use the find() method to determine the starting index of the word. Display a message if the word is not found.

sentence = input("Enter a sentence: ")
word = input("Enter a word: ")

index = sentence.find(word)
if index != -1:
    print(f"Word found at index: {index}")
else:
    print("Word not found.")
