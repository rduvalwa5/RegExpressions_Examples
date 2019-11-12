'''
https://docs.python.org/3/library/re.html
https://docs.python.org/3/library/re.html
https://docs.python.org/3/howto/regex.html



.
(Dot.) In the default mode, this matches any character except a newline. If the DOTALL flag has been specified, this matches any character including 
a newline.

^
(Caret.) Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.

$
Matches the end of the string or just before the newline at the end of the string, and in MULTILINE mode also matches before a newline. 
foo matches both ‘foo’ and ‘foobar’, while the regular expression foo$ matches only ‘foo’. More interestingly, searching for foo.$ in 'foo1\nfoo2\n' 
matches ‘foo2’ normally, but ‘foo1’ in MULTILINE mode; searching for a single $ in 'foo\n' will find two (empty) matches: one just before the newline, and one at the end of the string.

*
Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible. ab* will match ‘a’, ‘ab’, or ‘a’ 
followed by any number of ‘b’s.

+
Causes the resulting RE to match 1 or more repetitions of the preceding RE. ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not 
match just ‘a’.

?
Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. ab? will match either ‘a’ or ‘ab’.

*?, +?, ??
The '*', '+', and '?' qualifiers are all greedy; they match as much text as possible. Sometimes this behaviour isn’t desired; if the RE <.*> is 
matched against '<a> b <c>', it will match the entire string, and not just '<a>'. Adding ? after the qualifier makes it perform the match in 
non-greedy or minimal fashion; as few characters as possible will be matched. Using the RE <.*?> will match only '<a>'.

{m}
Specifies that exactly m copies of the previous RE should be matched; fewer matches cause the entire RE not to match. For example, a{6} will match 
exactly six 'a' characters, but not five.

{m,n}
Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many repetitions as possible. For example, 
a{3,5} will match from 3 to 5 'a' characters. Omitting m specifies a lower bound of zero, and omitting n specifies an infinite upper bound. As an 
example, a{4,}b will match 'aaaab' or a thousand 'a' characters followed by a 'b', but not 'aaab'. The comma may not be omitted or the modifier 
would be confused with the previously described form.

{m,n}?
Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as few repetitions as possible. This is the 
non-greedy version of the previous qualifier. For example, on the 6-character string 'aaaaaa', a{3,5} will match 5 'a' characters, while a{3,5}? 
will only match 3 characters.

\
Either escapes special characters (permitting you to match characters like '*', '?', and so forth), or signals a special sequence; special sequences 
are discussed below.

'''
import re

str = "The string is a big bad apple tree in a sentence.  Send sentence is this but with a xyz and lmnop.\n"
print(str)
print('1 ',re.match('The',str))
print('2' ,re.match(r'(.*)sentence', str, re.M))
print('3' ,re.match(r'(.+)sentence', str, re.M))
print('4' ,re.match(r'(.*)sentence', str))
print('5' ,re.match(r'(.+)sentence', str))
mch = re.match(r'(.*)sentence', str)
print('6 ', mch.group())
print('7 ', mch.group(0))
print('8 ', mch.group(1))
mch = re.match(r'(.*)x', str)
print('9 ', mch.group())
print('10 ', mch.group(0))
print('11 ', mch.group(1))
mch = re.match(r'(.*)a', str)
print('12 ', mch.group())
print('13 ', mch.group(0))
print('14 ', mch.group(1))
mch = re.match(r'(.*)but', str)
print('15 ', mch)
print('16 ', mch.group(0))
print('17 ', mch.group(1))
mch = re.match(r'(.*)T', str, re.M)
print(mch)

"""
$
Matches the end of the string or just before the newline at the end of the string, and in MULTILINE mode also matches before a newline. 
foo matches both ‘foo’ and ‘foobar’, while the regular expression foo$ matches only ‘foo’. More interestingly, searching for foo.$ in 'foo1\nfoo2\n' 
matches ‘foo2’ normally, but ‘foo1’ in MULTILINE mode; searching for a single $ in 'foo\n' will find two (empty) matches: one just before the newline,
and one at the end of the string.
"""

str1 = 'foo1\nfoo2\n'
mch = re.match(r'foo.$', str1, re.M)
print("foo ", mch)  #foo  <re.Match object; span=(0, 4), match='foo1'>

mch1 = re.match('(.*)foo1', str1)
print("foo1 ", mch1)
str2 = 'foo1 foo2\n'
mch2 = re.match(r'(.*)foo.$', str2, re.M)
print("foo2 ", mch2)