#Naive method

#importing the time package
import time

# Function to implement string searching
def bruteforce_search(pattern,text):
	pattern_len=len(pattern)   #length of pattern
	text_len=len(text)         #length of text
	no_of_searches=0  # To keep count of the searches
	for i in range(text_len - pattern_len +1):
		#Checking if the strings match
		for j in range(pattern_len): 
			if (text[i + j] != pattern[j]): 
				break
		#output the index at which the pattern is found
		if (j == pattern_len-1):  
			print("Pattern is found at index ", i)
			no_of_searches+=1
	#checking the ocurrences of pattern
	if(no_of_searches==0):
		print("pattern not found")
	else:
		print(no_of_searches," Results found")

#Fetching the file and reading the input from the file
txt=open("littlewomen.txt" ,"r")
string_txt=txt.readlines()
txt.close()
txt_len=0
text=""
#converting the input from list form to string form
for i in string_txt:
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
		#search the pattern using naive method, call to bruteforce_search function
		bruteforce_search(pattern,text)
		#End time of the execution
		finish = time.time() 
		#Output the amount of time taken to implement the algorithm
		print("Execution time =",(finish-start),"s")	




