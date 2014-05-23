###################This is a notepad for python exercises (http://greenteapress.com/thinkpython/html/)########################

#CHAPTER 8:Strings

#8.3 Traversal with a for loop
prefixes="JKLMNOPQ"
suffix="ack"
for i in prefixes:
     if i=="O" or i=="Q":
             print i+"u"+suffix
     else:
             print i+suffix
"""result: Jack Kack Lack Mack Nack Ouack Pack Quack"""

#8.6 Searching
def find(word,letter,index):
     while index<len(word):
             if word[index]==letter:
                     return index
             index=index+1
     return -1
 
find("dictionary","t",2)

#8.7 Looping and counting
def count(word,letter):
	count=0
	for i in word:
		if i==letter:
			count=count+1
	print count

>>> count("mississippi","s")
4

