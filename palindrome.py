####This small program is a tool to test whether a word is a palindrome#####

### Method 1 ###
def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	if len(word)<1:
		return True
	if first(word)!=last(word):
		return False
	return is_palindrome(middle(word))
	

### Method 2 ###:
def is_palindrome(word):
		if word==word[::-1]:
			return True
		else:
			return False

###### The exercise is from Thinkpython.com Chapter 6: Fruitful Function #####
	
