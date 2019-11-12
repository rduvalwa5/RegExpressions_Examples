'''
Created on Jan 18, 2019
^
(Caret.) Matches the start of the string, and in MULTILINE mode also matches immediately after 
each newline.
'''
import re

testString = "The quick brown fox jumped over the lAzy fox hound."

print(testString)

print("'The'  ",re.match(r'The', testString))
#  re.compile(r'^>([^\n\r]+)[\n\r]([A-Z\n\r]+)', re.MULTILINE
print("(.*)jumped  ",re.match(r'(.*)jumped', testString))

mtch = re.match(r'(.*)lazy fox', testString)
print("(.*)lazy fox   ",mtch)

mtch = re.match(r'(.*)lazy', testString)
print("(.*)lazy  ",mtch)

mtch = re.match(r'(.*)o', testString)
print("(.*)o  ",mtch)

mtch = re.match(r'(.*)+o', testString)
print("(.*)+o  ",mtch)

mtch = re.match(r'^(.*)T', testString)
print("^(.*)T  ",mtch)

mtch = re.match(r'(.*)[a-z]', testString)
print("[a-z]  ",mtch)

mtch = re.match(r'(.*)[1-9]', testString)
print("none [1-9]  ",mtch)

numString = "abcde gjkwpjf \
2345"\

mtch = re.match(r'(.*)[1-9]', numString)
print("[1-9]  ",mtch)

emStr = 'red1dog@reD.com'
print("emStr", emStr)
mtch = re.match(r'(.*)[a-z,A-Z]',emStr)
print("emStr1",mtch)
mtch = re.match(r'(.*)[a-z,A-Z,0-9]@[a-z,A-Z,0-9](.*)[com]',emStr)
print("emStr2",mtch)

emStr2 = 'red1dog@reD.gov'
print("emStr2", emStr2)
mtch = re.match(r'(.*)[a-z,A-Z]',emStr2)
print("emStr21",mtch)
mtch = re.match(r'(.*)[a-z,A-Z,0-9]@[a-z,A-Z,0-9](.*)[a-z(3)]',emStr2)
print("emStr22",mtch)