#Code and examples taken from: https://www.youtube.com/watch?v=K8L6KVGG-7o 
#watch this video for a full explanation of the code below 

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

#Raw strings (notice the difference)
# print('\tTab')
# print(r'\tTab')

# pattern = re.compile(r'abc')

#Searching for a period. Notice the difference
# pattern = re.compile(r'.')
# pattern = re.compile(r"\.")
# pattern - re.compile(r'coreyms\.com')

#Lets see the rest of the rules (see rules.txt)
pattern = re.compile(r'.') 
pattern = re.compile(r'\d') 
pattern = re.compile(r'\D') 
pattern = re.compile(r'\w') 
pattern = re.compile(r'\W') 
pattern = re.compile(r'\s') 
pattern = re.compile(r'\S') 

#anchors (see rules.txt)
pattern = re.compile(r'\bHa') #word boundary
pattern = re.compile(r'\BHa')
pattern = re.compile(r'^Start')
pattern = re.compile(r'^a') 
pattern = re.compile(r'$end')
pattern = re.compile(r'$a')  

#How to find patterns
pattern = re.compile(r'\d\d\d') 
pattern = re.compile(r'$\d\d\d.\d\d\d.\d\d\d\d') 
pattern = re.compile(r'$\d\d\d[-.]\d\d\d[-.]\d\d\d\d') #matching only phone numbers with dash and dot
pattern = re.compile(r'$[89]00[-.]\d\d\d[-.]\d\d\d\d') #find 800 or 900 numbers (try it with data.txt too!)

#Matching characters within a range using the dash symbol
pattern = re.compile(r'[1-5]')
pattern = re.compile(r'[a-z]')
pattern = re.compile(r'[a-z][A-Z]')
pattern = re.compile(r'^[a-z][A-Z]')
pattern = re.compile(r'[^b]at')

#how do we deal with multiple numbers of characters? with quantifiers! 
pattern = re.compile(r'$\d{3}.\d{3}.\d{4}') 
#other quantifiers
pattern = re.compile(r'Mr\.') #Mr. has to have a period
pattern = re.compile(r'Mr\.?') #period is optional
pattern = re.compile(r'Mr\.?\s[A-Z]\w+') #Doesn't match Mr. T
pattern = re.compile(r'Mr\.?\s[A-Z]\w*') #Now includes Mr. T

#matches = pattern.finditer(sentence)
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# #let's look at examples from data.txt
# #open data.txt
# with open('data.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)

