#### ROT 13 Encryption ####

""" Encryption Method:
Input: word (string), n (numeric)
Output: rotate the word by n letters
"""

def rot(word,n):
	index=0
	while index<len[word]:
		new=ord(word[index])+n
		letter=chr(new)
		return letter
	index=index+1


def rot_letter(l,n):
	if l.isupper():
		start=ord('A')
	elif l.islower():
		start=ord('a')
	else:
		return l
	c=ord(l)-start
	i=(c+n)%26+start      #The residue of division for 26 return the new position 
	return chr(i)


def rot_word(word,n):
	res=''
	for l in word:
		res +=rot_letter(l,n)  #use += to add all letters together
	return res


