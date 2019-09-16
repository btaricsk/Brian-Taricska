Create a list by calling the list() function with the following string "The quick brown fox jumps over the lazy dog." 
Convert all letters to lowercase before calling the list() function.
Sort the list.
Create a function called getMostFrequent() that outputs which letter(s) (excluding spaces) occurs the most often in the sentence. 
Indicate which letter and the in README.md.
Create another function called uniqueLetters() that creates a list of all unique characters in the string/list. 
Then it should ouput each unique character in order.


s = "The quick brown fox jumps over the lazy dog." 
print(s.lower())

import collections
print(collections.Counter(s).most_common(1)[0])

letters = "abcdefghijklmnopqrstuvwxyz"


def getMostFrequent(string):

    string = string.replace(" ", "").lower()

    total = 0

    for l in letters:
        count = string.count(l)
        if count > 1:
            total += count

    if total > 0:
        print("Duplicates found.")
    else:
        print("No duplicates found.")



 

   

