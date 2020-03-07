# Knuth-Morris_Pratt algorithm

#importing the time package
import time

# Function to implement string searching
def kmp_search(pattern,text):
	pattern_len = len(pattern) #length of pattern
	text_len = len(text)       #length of text
	lps=[0]*pattern_len   #Array to store the longest prefix suffix
	compute_prefix(pattern,pattern_len,lps)
	j=0   #index for traversing through pattern
	i = 0  #index for traversing through text
	no_of_searches=0 #To keep count of  the searches
	while i < text_len: 
		#checking if the strings match
		if pattern[j] == text[i]: 
			i += 1
			j += 1
		#output the index at which the pattern is found
		if j == pattern_len: 
			print("Found pattern at index " + str(i-j)) 
			no_of_searches+=1
			j = lps[j-1] 
		elif i < text_len and pattern[j] != text[i]: 
			if j != 0: 
				j = lps[j-1] 
			else: 
				i += 1
	#checking the occurrences of pattern
	if(no_of_searches==0):
		print("Pattern not found")
	else:
		print(no_of_searches," Results found")

#Function to preprocess the pattern
def compute_prefix(pattern, pattern_len, lps): 
	length = 0 
	lps[0] 
	i = 1
	#Calculating lps[i] from i=1 to pattern_len-1
	while i < pattern_len: 
		if pattern[i]== pattern[length]: 
			length += 1
			lps[i] = length
			i += 1
		else: 
			if length != 0: 
				length = lps[length-1] 
			else: 
				lps[i] = 0
				i += 1

#Fetching the file and reading the input from the file
txt=open("littlewomen.txt" ,"r")
string_text=txt.readlines()
txt.close()
text=""
#converting the input from list form to string form
for i in string_text:
    text+=i
#pattern to be searched
pattern = "Was it all self-pity, loneliness, or low spirits?  Or was it the waking\n"+"up of a sentiment which had bided its time as patiently as its\n"+"inspirer?  Who shall say?"
if(pattern==''):
	print("The pattern is empty, searching not required")
else:
	if(text==''):
		print("Text file is empty, cannot search the pattern")
	else:
		#Start time of the execution
		start = time.time()
		#search the pattern using kmp algorithm, call to kmp_search function
		kmp_search(pattern,text)
		#End time of the execution
		finish = time.time() 
		#Output the amount of time taken to implement the algorithm
		print("Execution time =",(finish-start),"s")	
