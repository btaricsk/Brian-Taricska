In this chapter, we're going to look at crypotanalysis, or the breaking of code. Code can be cracked using something called brute force, which means an attempt to crack the code using all the possibilities and combinations of words found in the dictionary. Various patterns can be found in both the transposition and substitution ciphers which give hackers an advantage to take a calculated attack. The rest of the chapter focuses on the different letters, and their combinations which help pair together phrases that may be used as authentication secrets. 

Create a file called Lab7.py. In this .py file you will complete the following coding exercises from the book. Please comment your solutions.
Exercise 8.9 (in the Chapter) - Now that you have seen the details of the railDecrypt function you can make it smarter in two ways:
You do not need to check cases where the number of rails is greater than the message length divided by two. Can you explain why?
After the rails have been fully written and identified, some combinations begin to repeat themself which is the reason the cases don't need to be checked. 

You only need to check cases where the number of rails evenly divides the total message length. Can you explain why?
This relates back to my previous answer. We want to find a list of rails that have the proper number:combination in order to make sure there is no repetition.

Exercise 8.14 (in the Chapter) - Write a function wordPop that accepts a text and a length N and returns the list of all the words that are N letters long, sorted by their length.
def wordPop(text, n):
    nwords = []
    words = text.split()
    
    for word in words: 
        if (len(word) <= n):
             nwords.append(word)
    nwords = sorted(nwords,cmp=length_compare)         
    return nwords

Exercise 8.18 - Write a regular expression pattern to match all words ending in ing.
import re
def find_ing(word):
    found = re.search('ing')
    if found:
        print(word, 'contains the letters "ing".')
    else:
        print(word, 'does not contain the letters "ing".')
	return ing


Exercise 8.20 - Write a regular expression pattern to match all words beginning and ending with the letter a.
import re
def find_'a'(word):
    found = re.search('begins with a')
    if found:
        print(word, 'this word beging with "a".')
    else:
        print(word, 'this word doesn't begin with "a".')
	return 'a'

When complete, push your Lab files to GitHub. Make sure it pushed successfully and then post the URL to your folder in comments sections of the Lab assignment.
