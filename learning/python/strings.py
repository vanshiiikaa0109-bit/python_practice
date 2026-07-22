msg = "I am learning topic - strings of Python"
print(msg)

#indexing and accessing
greet = "hello"
print(greet[0])
print(greet[4])
print(greet[2])
print(greet[:2])
print(greet[:4])
print(greet[-1])
print(greet[-4])

#properties

#1.immutable
s = "hello"
#s[0] = "M" #rejected shows error
s = "Bye" #it can be changed because s is a string

#2.concatenation
msg1 = "hello"
msg2 = "dear"
msg3 = msg1+msg2
print(msg3)

#3.replication
print('='*50)

#4.character checking
print('e' in 'hello')
print('v' in 'hello')

#functions

msg = 'Vanshika' 
print(len(msg))
print(min(msg)) #prints character with min value
print(max(msg))

#methods - when we create a string a nameless object of type 'str' is created
msg = 'xyz'
print(type(msg))
print(id(msg)) #prints address of msg object

s = 'Hello'
print(s.upper()) #syntax - string.methpd()
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.islower())
print(s.isupper())
print(s.startswith('a'))
print(s.endswith('a'))
print(s.find("H"))
print(s.replace("H","m"))

#stripping
text = "   Hello   "
print(text.lstrip()) # left strippiing

text1 = "##hello##"
print(text1.lstrip('#'))

text = "   Hello   "
print(text.strip()) #both side stripping

text1 = "##hello##"
print(text1.strip('#')) 

text = "   Hello   "
print(text.rstrip()) # right stripping

text1 = "##hello##"
print(text1.rstrip('#'))

#splitting
text2 = "Hello World"
print(text2.split(' ')) # split(',') -> splits at commas
                        #split(' ') or split() -> splits at spaces

# partition 
text = "hell0 world python i like to study you"
print(text.partition(' ')) # jo seperator hum bolenge vo jaha bhi present hoga vha partition hoga - partition string in 3 parts at first occurence of specified string

#join 
msg = "hello"
print(msg.replace("h","m"))
print("-".join("hello"))

#string conversions
msg = "hEllo"
print(msg.upper())
print('Hello'.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())
print(msg.swapcase())

age = 25
print("she is" + str(age) +"years old")
i = int("34")
f = float("3.14")
c = complex("2+3j")
print(ord('A'))  #print 65
print(chr(65))   #print A

#string comparison
s1 = "Bombay"
s2 = "bombay"
s3 = "Nagpur"
s4 = "Bombaywala"
s5 = "Bombay"
print(s1 == s2)
print(s1 == s5)
print(s1 != s3)
print(s1 >s5)
print(s1 <s2)
print(s1 <= s4)

#regular Expression = used for validating input(checking input pattern against acceptable patterns)

import re
s = 'Bombaywala'
print(re.search('bay',s))

import re
text = "Hello Python"
print(re.match("Hello", text))
print(re.match("Python", text))

import re
text = "cat bat mat cat"
print(re.findall("cat", text))

import re
text = "I like cats"
new = re.sub("cats", "dogs", text)  #replaces matched text
print(new)

import re
text = "apple,banana;grapes"
print(re.split("[,;]", text))

# Regular Expressions (Regex) Metacharacters in Python

import re

text = "Hello 123 World abc@gmail.com color colour ac abc abbc"
# 1. . (Dot) - Matches any single character
print("1. Dot (.):", re.findall(r"a.c", text))
# Matches: abc

# 2. ^ (Caret) - Matches the beginning of the string
print("2. Starts with Hello:", re.search(r"^Hello", text))
# Checks whether the string starts with "Hello"

# 3. $ (Dollar) - Matches the end of the string
print("3. Ends with abbc:", re.search(r"abbc$", text))
# Checks whether the string ends with "abbc"

# 4. * (Star) - Zero or more occurrences
print("4. * :", re.findall(r"ab*c", text))
# Matches: ac, abc, abbc

# 5. + (Plus) - One or more occurrences
print("5. + :", re.findall(r"ab+c", text))
# Matches: abc, abbc (NOT ac)

# 6. ? (Question Mark) - Zero or one occurrence
print("6. ? :", re.findall(r"colou?r", text))
# Matches: color and colour

# 7. [] (Character Set)
print("7. Character Set:", re.findall(r"[aeiou]", text))
# Finds all vowels

# 8. [^ ] (Negated Character Set)
print("8. Not Digit:", re.findall(r"[^0-9 ]", "abc123"))
# Finds all non-digit characters

# 9. | (OR Operator)
print("9. OR:", re.findall(r"Hello|World", text))
# Matches either Hello or World

# 10. () (Grouping)
print("10. Grouping:", re.findall(r"(ab)+", "ab abab"))
# Matches grouped pattern "ab"

# 11. {} (Repetition)
print("11. Repetition:", re.findall(r"a{2,3}", "a aa aaa aaaa"))
# Matches aa or aaa

# 12. \d (Digit)
print("12. Digits:", re.findall(r"\d", text))
# Finds all digits

# 13. \D (Non-Digit)
print("13. Non-Digits:", re.findall(r"\D", "abc123"))

# 14. \w (Word Character)
print("14. Words:", re.findall(r"\w+", text))
# Finds words, digits and underscore

# 15. \W (Non-Word Character)
print("15. Non-Word:", re.findall(r"\W", "Hello@123"))

# 16. \s (Whitespace)
print("16. Spaces:", re.findall(r"\s", text))

# 17. \S (Non-Whitespace)
print("17. Non-Spaces:", re.findall(r"\S", text))

# 18. Escape Character (\)
print("18. Dot Symbol:", re.findall(r"\.", "www.google.com"))
# Matches literal '.' instead of any character

# 19. Email Validation
email = "abc@gmail.com"

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("19. Valid Email")
else:
    print("19. Invalid Email")