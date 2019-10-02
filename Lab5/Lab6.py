Complete exercise 7.1: Write a function that prints the numbers from 0 to 50 counting by 5. This function must use a while loop.

counter = 5
while counter < 51:
print(counter)
counter = counter + 5


Complete exercise 7.2: Write a function that takes a string as a parameter and returns the number of spaces in the string. 
This function must use a while loop.
string = 'My name is Brian'
count=0

for a in string: 
    if (a.isspace()) == True: 
        count+=1
print(count) 
  
string = 'My name is \n\n\n\n\nBrian'
count = 0
for a in string: 
while (a.isspace()) == True: 
        count+=1
print(count) 

Complete exercise 7.3: Write a function that asks the user to enter exam scores one at a time until the word stop is entered. 
When stop is entered, the program should compute the average of the scores.

def examscores()
examscores = []

# Set new_name to 'stop'
new_name = 'stop'

# Start a loop that will run until the user enters 'quit'.
while new_name != 'stop':
    # Ask the user for a name.
    new_name = input("enter 'stop' ")

    # Add the new name to our list.
    if new_name != 'stop':
        examscores.append(new_name)

# Show that the name has been added to the list.
print(examscores)


Complete exercise 7.4: Write a function that takes a string as a parameter and returns True if the string is a palindrome, and 
False otherwise. This function should use a while loop. Hint: A palindrome is a word that is spelled
    
def isPalindrome(st) : 
    n = len(st) 
      
    # An empty string is  
    # considered as palindrome 
    if (n == 0) : 
        return True
      
    return isPalRec(st, 0, n - 1); 
 
# Driver Code 
st = "deed"
if (isPalindrome(st)) : 
    print "Yes"
else : 
    print "No"
