import re
string="""Hello my Number is 6363313934 and
my friend's number is 9731603162"""

regex='\d+'
match = re.findall(regex, string)
print(match)