
In your README.md file, describe - in a few sentences - what we've covered in lesson 3.
Chapter 3 covered a variety of subjects, and can be narrowed down to strings and cryptography. For strings, we looked at how to concatenate a string, how to index and repeat a string which is important to understand when getting into cryptography. Cryptography is synonymous with "secret." Secrets come in the form of either transpositioning the string or having a key. A key is beneficial because it is inherently more secure or "a more difficult secret to crack," but does involve more overhead with its creation and implementation. Keys come in various forms and certain algorithms, such as the Vignere algorithm, are used.

Again, in README.md, answer the following questions:
List and describe 3 basic string methods.
1)Count: the count method is able to determine the number of occurances of one string inside another
2)Index: returns the substring if the string is found; if not found, it returns with an error
3)Find:Similar to index, but if not found, it returns with a "1"

Describe the 3 simple algorithms for encryption that we covered in this lesson (it can be in 2 or 3 sentences.
We learned about the transposition, substitution and vignere ciphers in chapter 3. The Transposition cipher is a matter of shifting and replacing characters, substitution replaces and the vignere cipher implements a key for each letter as opposed to strings. 
Identify the type of encryption the following algorithm is implementing:
def encrypt(plainText ,key):  
  alphabet = "abcdefghijklmnopqrstuvwxyz"  
  plainText = plainText.lower ()  
  cipherText = ""  

  for ch in plainText:  
      idx = alphabet.find(ch)  
      cipherText = cipherText + key[idx]  
  return cipherText  
  
This is using the substitution algorithm. 

Identify the type of encryption the following algorith is implementing:
def scramble2Encrypt(plainText):  
  evenChars = ""  
  oddChars = ""  
  charCount = 0  

  for ch in plainText:  
      if charCount % 2 == 0:  
          evenChars = evenChars + ch  
      else:  
          oddChars = oddChars + ch  
    charCount = charCount + 1  
  cipherText = oddChars + evenChars  
  
  This is using the transposition algorithm. 
